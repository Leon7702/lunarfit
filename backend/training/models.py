from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

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


class Trs(models.Model):
    """
    Training Readiness Score data for a certain user and day.
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    acwr = models.FloatField()
    trs_acwr = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(6)]
    )
    mood = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(6)]
    )
    complaints = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(6)]
    )
    recovery = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(6)]
    )
