from datetime import date, timedelta

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.db.models import Avg, F, Sum

from users.models import User


class Sport(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Workout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sport = models.ForeignKey(Sport, on_delete=models.SET_NULL, null=True, blank=True)
    start = models.DateTimeField()
    duration = models.PositiveSmallIntegerField()
    intensity = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)]
    )

    def __str__(self):
        return f"{self.user}: {self.start} for {self.duration}min sport: {self.sport}"

    def save(self, *args, **kwargs):
        # save first, so the value is available for updates
        super().save(*args, **kwargs)
        self.update_next_acwr()

    def delete(self):
        # delete first, so the value is not used for updates
        print(f"pre deleting {self}")
        super().delete()
        print(f"post deleting {self}")
        self.update_next_acwr()

    def update_next_acwr(self):
        """
        Updates the ACWR values of the nearest future TRS Log, including on the day of the workout.
        It only updates a single entry, the TRS model takes care of cascading the changes to all future entries,
        as this is only necessary once.
        """
        first_trs_entry_from_today = (
            self.user.trs_set.filter(date__gte=self.start.date())
            .order_by("date")
            .first()
        )
        print(f"TRS to update {first_trs_entry_from_today}")
        # it is possible there is no daily assessment for the workout day, use the nearest future one
        # acwr update will cascade from there
        if first_trs_entry_from_today:
            first_trs_entry_from_today.update_acwr()


class Trs(models.Model):
    """
    Training Readiness Score data for a certain user and day.
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    acwr = models.FloatField(editable=False)
    trs_acwr = models.PositiveSmallIntegerField(editable=False)
    mood = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(6)]
    )
    complaints = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(6)]
    )
    recovery = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(6)]
    )

    def __str__(self):
        return f"{self.user}, {self.date}"

    def get_previous_trs(self):
        return Trs.objects.filter(date__lt=self.date).order_by("-date").first()

    def get_trs_acwr(self) -> int:
        previous_trs = self.get_previous_trs()
        if not previous_trs:
            return 6

        if self.acwr > 1.8:
            penalty = -2
        elif self.acwr > 1.5:
            penalty = -1
        else:
            return 6

        trs_acwr = previous_trs.trs_acwr + penalty
        if trs_acwr < 0:
            return 0

        return trs_acwr

    def aggregate_workouts(
        self, start_date: date, end_date: date
    ) -> models.query.QuerySet:
        """
        Returns a queryset of workouts, aggregated by days, annotated with the rpe__avg of the day.
        It could be an empty queryset. Dates are inclusive.
        """
        return (
            self.user.workout_set.filter(start__date__range=(start_date, end_date))
            .annotate(rpe=F("intensity") * F("duration"))
            .values("start__date")
            .annotate(Avg("rpe"))
        )

    def user_has_logged_workouts_from(self, start_date: date) -> bool:
        return self.user.workout_set.filter(start__date__lte=start_date).exists()

    def get_workload(self, end_date: date, days: int) -> float:
        """
        Returns the average workload for a date range, taking onboarding data into account as necessary.
        end_date is the newer date of the date range, should be the day of the acwr entry.
        days are the number of days to include, usually 7 or 28.
        """
        start_date = end_date - timedelta(days - 1)
        workouts = self.aggregate_workouts(start_date, end_date)
        workload = 0

        if workouts.exists():
            workload = workouts.aggregate(workload=Sum("rpe__avg"))["workload"]

        if (
            self.user_has_logged_workouts_from(start_date)
            or not self.user.profile.onboarding_finished
        ):
            return workload / days

        onboarding = self.user.onboarding
        OFFSET = timedelta(days=2)
        # Add two additional days for which the workload should not
        # be factored from the onboarding average.
        # the first daily assessment on the day of the onboarding would ask
        # for the day before the onboarding + the onboarding day itself

        onboarding_daily_workload = (
            onboarding.workout_duration
            * onboarding.workout_intensity
            * onboarding.workout_frequency
            / 7
        )

        logged_days = (end_date - onboarding.timestamp + OFFSET).days

        if logged_days < 1:
            return onboarding_daily_workload

        onboarding_days = days - logged_days
        logged_workload = workload / logged_days

        # factor in the onboarding workload average,
        # weighted by the number of day that entries could be logged
        workload = (
            onboarding_daily_workload * onboarding_days + logged_workload * logged_days
        )
        return workload / days

    def get_acwr(self) -> float:
        acute_workload = self.get_workload(self.date, 7)
        chronic_workload = self.get_workload(self.date, 28)

        if chronic_workload == 0:
            return 1
        else:
            return acute_workload / chronic_workload

    def save(self, *args, update_fields=None, **kwargs):
        self.acwr = self.get_acwr()
        self.trs_acwr = self.get_trs_acwr()
        super().save(*args, update_fields=update_fields, **kwargs)

    def update_acwr(self) -> None:
        future_trs_entries = self.user.trs_set.filter(date__gte=self.date)
        for entry in future_trs_entries:
            entry.save(update_fields=["acwr", "trs_acwr"])
