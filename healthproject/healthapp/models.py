from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
    pass


class Exercise(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100, default='')
    cal_bun = models.FloatField(default=0.0)
    image = models.CharField(max_length=100000, default="")
    desc = models.TextField()
    link = models.CharField(max_length=2000, null=False)

    def __str__(self):
        return self.name


class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="appointment")
    full_name = models.CharField(max_length=200)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=13)
    desc = models.TextField()
    address = models.TextField()
    pincode = models.CharField(max_length=6)
    timeStamp = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return f'Appointment of {self.full_name}'


class Calorie(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="calorie")
    calorie_burnt = models.FloatField(default=0.0)
    date = models.DateField(auto_now=True, blank=True)

    def __str__(self):
        return f'{self.calorie_burnt}'