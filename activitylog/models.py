from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core.mail import send_mail
from datetime import datetime

from .managers import UserManager

class User(AbstractBaseUser, PermissionsMixin):
    # email = models.EmailField(unique=True)
    login = models.CharField(max_length=200, unique=True)
    password = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    second_name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()
    USERNAME_FIELD = 'login'
    REQUIRED_FIELDS = []

    # def email_user(self, subject, message, from_email=None, **kwargs):
    #     '''
    #     Отправляет электронное письмо этому пользователю.
    #     '''
    #     send_mail(subject, message, from_email, [self.email], **kwargs)

    def __str__(self):
        return self.login

class Car(models.Model):
    name = models.CharField(max_length=200, unique=True)
    car_number = models.CharField(max_length=200, unique=True)
    all_mileage = models.FloatField(default=0.0, help_text='km.m')
    busy = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class UserCar(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    car = models.ForeignKey(Car, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.user.login + " | " + self.car.name

class ActivityLog(models.Model):
    user_car = models.ForeignKey(UserCar, on_delete=models.SET_NULL, null=True)
    get_time = models.DateTimeField(default=datetime.now)
    return_time = models.DateTimeField(blank=True, null=True)
    travel_target_point = models.TextField(blank=True)
    travel_mileage = models.FloatField(default=0.0, help_text='km.m')

    def __str__(self) -> str:
        return super().__str__()