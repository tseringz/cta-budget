from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db.models.signals import post_save
from django.dispatch import receiver


class User(AbstractUser):

    class Role(models.TextChoices):
        ADMIN = "ADMIN", "Admin"
        ACCOUNTANT = "ACCOUNTANT", "Accountant"
        SECRETARY = "SECRETARY", "Secretary"

    base_role = Role.ADMIN

    role = models.CharField(max_length=50, choices=Role.choices)
    avatar = models.ImageField(
        upload_to="images/avatars")

    def save(self, *args, **kwargs):
        if not self.pk:
            self.role = self.base_role
            return super().save(*args, **kwargs)


class AccountantManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.ACCOUNTANT)


class Accountant(User):

    base_role = User.Role.ACCOUNTANT
    accountant = AccountantManager()

    class Meta:
        proxy = True

    def welcome(self):
        return "Only for accountant"


@receiver(post_save, sender=Accountant)
def create_user_profile(sender, instance, created, **kwargs):
    if created and instance.role == "ACCOUNTANT":
        AccountantProfile.objects.create(user=instance)


class AccountantProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    accountant_id = models.IntegerField(null=True, blank=True)


class SecretaryManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.SECRETARY)


class Secretary(User):
    base_role = User.Role.SECRETARY
    secretary = SecretaryManager()

    class Meta:
        proxy = True

    def welcome(self):
        return "Only for secretary"


@receiver(post_save, sender=Secretary)
def create_user_profile(sender, instance, created, **kwargs):
    if created and instance.role == "SECRETARY":
        SecretaryProfile.objects.create(user=instance)


class SecretaryProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    secretary_id = models.IntegerField(null=True, blank=True)
