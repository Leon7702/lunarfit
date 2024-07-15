from django.db import models

from users.models import User


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
    name = models.CharField(max_length=24)
    description = models.CharField(max_length=512)
    interfered_days = models.IntegerField()
    contraception = models.BooleanField()


class Medication(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    medication_id = models.ForeignKey(MedicationCategory, on_delete=models.CASCADE)
