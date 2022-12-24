from django.db import models
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel


class Skills(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Specialties(MPTTModel):
    name_uz = models.CharField(max_length=100)
    name_ru = models.CharField(max_length=100)
    name_en = models.CharField(max_length=100)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, related_name='children')

    def __str__(self):
        return self.name_uz
