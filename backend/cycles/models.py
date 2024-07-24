from django.db import models

from users.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone


class MenstrualCycle(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start = models.DateField()
    end = models.DateField()

    def __str__(self):
        return f"{self.cycle_id}, {self.user.email}"


class Phase(models.Model):
    PHASES = [
        (0, "Menstruation"),
        (1, "Follicular"),
        (2, "Ovulation"),
        (3, "Early Luteal"),
        (4, "Late Luteal"),
    ]
    cycle_id = models.ForeignKey(MenstrualCycle, on_delete=models.CASCADE)
    start = models.DateField()
    end = models.DateField()
    phase_number = models.PositiveIntegerField(choices=PHASES)

    def __str__(self):
        return f"{self.phase_number}, {self.cycle_id}, {self.user.email}"


class MedicationCategory(models.Model):
    name = models.CharField(max_length=50)


class Medication(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    medication_id = models.ForeignKey(MedicationCategory, on_delete=models.CASCADE)


class Type(models.Model):
    name = models.CharField(max_length=24)
    

class TrackingData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    date = models.DateField()
    value = models.DecimalField(max_digits=4, decimal_places=2)


@receiver(post_save, sender=TrackingData)
def create_menstrual_cycle(sender, instance, created, **kwargs):
    if created and instance.type.id == 1: 
        user=instance.user
        start_date = instance.date
        end_date = start_date + timezone.timedelta(days=28) 

        latest_cycle = MenstrualCycle.objects.filter(user=user).order_by('-start').first()
        
        previous_day = start_date - timezone.timedelta(days=1)
        previous_day_entry = TrackingData.objects.filter(user=user, type=1, date=previous_day).exists()


        if (latest_cycle is None or (timezone.now().date() - latest_cycle.start).days >= 14) and not previous_day_entry:
            menstrual_cycle = MenstrualCycle.objects.create(
                user=user,
                start=start_date,
                end=end_date
            )

            Phase.objects.create(
                cycle=menstrual_cycle,
                start=start_date,
                end=start_date + timezone.timedelta(days=5),
                phase_number=0
            )
        