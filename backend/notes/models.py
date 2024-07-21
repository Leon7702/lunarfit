from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from users.models import User


class SymptomCategory(models.Model):
    name = models.CharField(max_length=24, null=False)
    description = models.CharField(max_length=512)

    def __str__(self):
        return f"{self.name}, {self.description}, {self.symptom_category}"


class Symptom(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    symptom_category = models.ForeignKey(SymptomCategory, on_delete=models.CASCADE)
    day = models.DateField()
    value = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(6)]
    )

    def __str__(self):
        return f"{self.day}, {self.value}, {self.symptom_category}"


class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    content = models.CharField(max_length=1024)
