from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.log_in, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.log_out, name='logout'),
    path('cars/', views.cars_view, name='cars'),
    path('activitylog/', views.activitylog_view, name='activitylog'),
    path('user_car_registr/', views.user_car_registr, name='user_car_registr'),
    path('user_create_activitylog/', views.user_create_activitylog, name='user_create_activitylog'),
    path('user_update_activitylog/{id}', views.user_update_activitylog, name='user_update_activitylog'),
]