from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import MinValueValidator, MaxValueValidator


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        return self.create_user(email, password, **extra_fields)


class Contraceptive(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=512)
    show_hint = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    finished_onboarding = models.BooleanField(default=False)
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    birthdate = models.DateField(null=True, blank=True)
    body_weight = models.DecimalField(
        max_digits=4, decimal_places=1, null=True, blank=True
    )
    body_height = models.PositiveSmallIntegerField(null=True, blank=True)
    # IETF Lang Code: https://www.rfc-editor.org/rfc/rfc5646#section-4.4.1
    language = models.CharField(max_length=35, default="de")
    contraceptive = models.ForeignKey(
        Contraceptive, on_delete=models.SET_NULL, null=True, blank=True
    )

    def __str__(self):
        return f"{self.last_name}, {self.first_name}: {self.user.email}"


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save


class MenstrualCycle(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start = models.DateField()
    end = models.DateField()

    def __str__(self):
        return f"{self.cycle_id}, {self.user.email}"


class Phase(models.Model):
    PHASES = [(0, 'Menstruation'), (1, 'Follicular'), (2, 'Ovulation'), (3, 'Early Luteal'), (4, 'Late Luteal')]
    cycle_id = models.ForeignKey(MenstrualCycle, on_delete=models.CASCADE)
    start = models.DateField()
    end = models.DateField()
    phase_number = models.PositiveIntegerField(choices=PHASES)

    def __str__(self):
        return f"{self.phase_number}, {self.cycle_id}, {self.user.email}"


class SymptomCategory(models.Model):
    name = models.CharField(max_length=24, null=False)
    description = models.CharField(max_length=512)

    def __str__(self):
        return f"{self.name}, {self.description}, {self.symptom_category}"


class Symptom(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    symptom_category = models.ForeignKey(SymptomCategory, on_delete=models.CASCADE) 
    date = models.DateField()
    value  = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(6)])

    def __str__(self):
        return f"{self.day}, {self.value}, {self.symptom_category}"


class MedicationCategory(models.Model):
    name = models.CharField(max_length=24)
    description = models.CharField(max_length=512)
    interfered_days = models.IntegerField()
    contraception = models.BooleanField()


class Medication(models.Model):
     user = models.ForeignKey(User, on_delete=models.CASCADE)
     start = models.DateField()
     end = models.DateField()
     medication_id = models.ForeignKey(MedicationCategory, on_delete=models.CASCADE)


class  Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    content = models.CharField(max_length=1024)