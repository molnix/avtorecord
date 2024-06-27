from django.db import models
import datetime

class Car(models.Model):
    name = models.CharField(max_length=200, unique=True)
    all_mileage = models.FloatField(default=0.0, help_text='km.m')
    busy = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class User(models.Model):
    email = models.CharField(max_length=200, unique=True)
    login = models.CharField(max_length=200, unique=True)
    password = models.CharField(max_length=200) 

    def __str__(self):
        return self.login


class ActivityLog(models.Model):
    car = models.ForeignKey(Car, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    get_time = models.DateTimeField(auto_now_add=True)
    return_time = models.DateTimeField(blank=True)
    travel_start_point = models.TextField(blank=True)
    travel_target_point = models.TextField(blank=True)
    travel_mileage = models.FloatField(default=0.0, help_text='km.m')

    def __str__(self) -> str:
        return super().__str__()