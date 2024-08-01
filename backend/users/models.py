from datetime import date

from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


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
    onboarding_finished = models.BooleanField(default=False)
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
    instance.profile.save()


class Onboarding(models.Model):
    """
    This model separates onboarding data from the user profile, as it is only used during the initial months.
    As more data becomes available, rolling averages should be used instead of the initial estimates.
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    timestamp = models.DateField(default=date.today, blank=True)
    workout_frequency = models.PositiveSmallIntegerField(default=0)
    workout_duration = models.PositiveSmallIntegerField(default=0)
    workout_intensity = models.PositiveSmallIntegerField(default=0)
    cycle_duration = models.PositiveSmallIntegerField(default=29)
    menstruation_duration = models.PositiveSmallIntegerField(default=4)

    def __str__(self):
        return f"{self.user.email}, {self.timestamp}"


@receiver(post_save, sender=Onboarding)
def finish_onboarding(sender, instance, created, **kwargs):
    instance.user.profile.onboarding_finished = True
    instance.user.profile.save()
