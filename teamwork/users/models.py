from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from .managers import UserManager
from teamwork.skills.models import Specialties, Skills


class User_Type(models.IntegerChoices):
    EMPLOYEE = 1, _('EMPLOYEE')
    EMPLOYER = 2, _('EMPLOYER')


class JINS(models.IntegerChoices):
    ERKAK = 1, _('ERKAK')
    AYOL = 2, _('AYOL')


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
    specialty = models.ForeignKey(Specialties, on_delete=models.CASCADE)
    skills = models.ManyToManyField(Skills, related_name='employee_skills')
    job_address = models.CharField(max_length=100)
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=100)

    # Other Info
    passport = models.CharField(max_length=9, null=True, blank=True)
    email = models.EmailField(max_length=70, blank=True, unique=True, null=True)
    birth_date = models.DateField(null=True, blank=True)
    jins = models.IntegerField(default=JINS.ERKAK, choices=JINS.choices, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.user.phone + ' ' + self.user.name


class Employer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    organazation_name = models.CharField(max_length=100)
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=100)
    employee_count = models.IntegerField()

    def __str__(self):
        return self.user.phone + ' ' + self.user.name
