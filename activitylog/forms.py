from .models import Car, User, ActivityLog, UserCar
from django import forms
#Model Forms
class UserCreateForm(forms.Form):
    model = User
    login = forms.CharField(label='Логин')
    first_name = forms.CharField(label='Имя')
    second_name = forms.CharField(label='Фамилия')
    surname = forms.CharField(label='Отчество')
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput())
    
class UserLoginForm(forms.Form):
    model = User
    login = forms.CharField(label='Логин')
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput())
class CarForm(forms.Form):
    model = Car
    name = forms.CharField(label='Название автомобиля')
    car_number = forms.CharField(label='Государственный номер')
    all_mileage = forms.FloatField(label='Пробег км')
class ActivityLogForm(forms.Form):
    model = ActivityLog
    user_car = forms.CharField(label='Автомобиль')
    return_time = forms.DateTimeField(label='Дата и время возвращения')
    travel_target_point = forms.CharField(label='Точка назначения')
    travel_mileage = forms.CharField(label='Пробег автомобиля за поездку км')
class UserCarForm(forms.Form):
    model = UserCar
    user = forms.IntegerField(label='Водитель')
    car = forms.IntegerField(label='Автомобиль')