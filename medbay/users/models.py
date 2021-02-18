from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    is_doctor = models.BooleanField('doctor status',default=False)
    is_patient = models.BooleanField('teacher status',default=False)


class Doctor(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    registrationNumber = models.PositiveIntegerField(null=True,blank=True)

    def __str__(self) -> str:
        return self.user.username

class Patient(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)