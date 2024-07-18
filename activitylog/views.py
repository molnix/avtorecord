from django.shortcuts import render
from django.contrib.auth import logout, authenticate, login
from django.shortcuts import redirect
from django.views import generic
from .models import ActivityLog, User, Car
from .forms import *
from datetime import datetime

def index(request):
    cars = Car.objects.all()
    activitylogs = ActivityLog.objects.all()

    return render(
        request,
        'index.html',
        context= {
            'cars' : cars,
            'activitylogs' : activitylogs,
        }
    )

def log_in(request):
    if request.method == "POST":
        user = authenticate(request=request, username=request.POST.get("login"), password=request.POST.get("password"))
        if user is not None:
            login(request, user)
            print("login")
            return redirect("index")
        else:
            print("No")
            return redirect("login")
    return render(request, 'login.html', context={'UserLoginForm' : UserLoginForm()})
    
def register(request):
    users = User.objects.all()
    if request.method == "POST":
        user = User()
        # user.email = request.POST.get("email")
        user.login = request.POST.get("login")
        user.first_name = request.POST.get("first_name")
        user.second_name = request.POST.get("second_name")
        user.surname = request.POST.get("surname")
        user.set_password(request.POST.get("password"))
        user.save()
        return redirect("register")
    return render(request, 'register.html', context={ 'UserCreateForm' : UserCreateForm(), 'users' : users})

def log_out(request):
    logout(request)
    return redirect("index")

def cars_view(request):
    cars = Car.objects.all()
    car_form = CarForm()
    if request.method == "POST":
        car = Car()
        car.name = request.POST.get("name")
        car.car_number = request.POST.get("car_number")
        car.all_mileage = request.POST.get("all_mileage")
        car.save()
        return redirect("cars")
    return render(request, 'cars.html', context = {'cars' : cars, 'CarForm' : car_form})

def activitylog_view(request):
    users = User.objects.all()
    cars = Car.objects.all()
    activitylogs = ActivityLog.objects.all()
    users_cars = UserCar.objects.all()
    
    user_cars = UserCar.objects.filter(user = request.user.id)
    user_cars_id = []
    for u in user_cars:
        user_cars_id.append(u.id)
    user_logs = []
    for log in activitylogs:
        if log.user_car.id in user_cars_id:
            user_logs.append(log)
    
    return render(request, 'activitylog.html', 
    context = {
        'activitylogs' : activitylogs,
        'userscars' : users_cars,
        'users' : users,
        'cars' : cars,
        'user_logs' : user_logs,
        'user_cars' : user_cars})

def user_car_registr(request):
    if request.method == "POST":
        user = User.objects.get(id = int(request.POST.get("user")))
        car = Car.objects.get(id = int(request.POST.get("car")))
        user_car = UserCar()
        user_car.user = user
        user_car.car = car
        user_car.save()
    return redirect('activitylog')

def user_create_activitylog(request):
    if request.method == "POST":
        activitylog = ActivityLog()
        usercar = UserCar.objects.get(car = int(request.POST.get("usercar")), user = request.user.id)
        car = Car.objects.get(id = int(request.POST.get("usercar")))
        car.busy = True
        car.save()
        activitylog.user_car = usercar
        activitylog.travel_target_point = request.POST.get("travel_target_point")
        print(car)
        activitylog.save()
    return redirect('activitylog')

def user_update_activitylog(request):
    if request.method == "GET":
        activitylog = ActivityLog.objects.get(id = int(request.GET.get("id")))
        activitylog.return_time = datetime.now()
        activitylog.save()
    return redirect('activitylog')