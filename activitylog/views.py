from django.shortcuts import render
from django.contrib.auth import logout, authenticate, login
from django.shortcuts import redirect
from django.views import generic
from .models import ActivityLog, User, Car

def index(request):
    cars = Car.objects.filter(busy=False)
    activitylogs = ActivityLog.objects.all()

    return render(
        request,
        'index.html',
        context= {
            'cars' : cars,
            'activitylogs' : activitylogs,
        }
    )

def login(request):
    if request.method == "POST":
        user = authenticate(request=request, login=request.POST.get("login"), password=request.POST.get("password"))
        if user is not None:
            login(request, user)
            return redirect("index")
        else:
            print(user)
            return redirect("login")
    return render(request, 'login.html', context={})
    
def register(request):
    if request.method == "POST":
        user = User()
        user.email = request.POST.get("email")
        user.login = request.POST.get("login")
        user.password = request.POST.get("password")
        user.save()
        return redirect("login")
    return render(request, 'register.html', context={})


def log_out(request):
    logout(request)
    return redirect("index")
