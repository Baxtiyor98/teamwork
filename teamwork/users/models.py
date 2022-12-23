from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from teamwork.users.managers import UserManager


class User_Type(models.IntegerChoices):
    EMPLOYEE = 1, _('EMPLOYEE')
    EMPLOYER = 2, _('EMPLOYER')


class User(AbstractUser):
    username = None
    first_name = None
    last_name = None

    name = models.CharField(_("Name of User"), max_length=255)
    phone = models.CharField(_("Phone"), unique=True, max_length=13)
    type = models.IntegerField(default=User_Type.EMPLOYEE, choices=User_Type.choices)
    image = models.ImageField(_("Image"), upload_to='user_image', null=True, blank=True)

    objects = UserManager()

    USERNAME_FIELD = "phone"
    REQUIRED_FIELDS = ["name"]

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"phone": self.phone})


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.phone + ' ' + self.user.name


class Employer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.phone + ' ' + self.user.name
