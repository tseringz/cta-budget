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

    role = models.CharField(max_length=50, choices=Role.choices, default=base_role)
    avatar = models.ImageField(upload_to="images/avatars", null=True, blank=True)
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_groups',
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions',
        blank=True
    )

    def save(self, *args, **kwargs):
        if not self.pk:
            self.role = self.base_role
        super().save(*args, **kwargs)


class AccountantManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(role=User.Role.ACCOUNTANT)


class Accountant(User):
    base_role = User.Role.ACCOUNTANT
    objects = AccountantManager()

    class Meta:
        proxy = True

    def welcome(self):
        return "Only for accountant"


class SecretaryManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(role=User.Role.SECRETARY)


class Secretary(User):
    base_role = User.Role.SECRETARY
    objects = SecretaryManager()

    class Meta:
        proxy = True

    def welcome(self):
        return "Only for secretary"


class AccountantProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    accountant_id = models.IntegerField(null=True, blank=True)


class SecretaryProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    secretary_id = models.IntegerField(null=True, blank=True)


@receiver(post_save, sender=Accountant)
def create_accountant_profile(sender, instance, created, **kwargs):
    if created and instance.role == User.Role.ACCOUNTANT:
        AccountantProfile.objects.create(user=instance)


@receiver(post_save, sender=Secretary)
def create_secretary_profile(sender, instance, created, **kwargs):
    if created and instance.role == User.Role.SECRETARY:
        SecretaryProfile.objects.create(user=instance)
