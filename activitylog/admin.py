from django.contrib import admin
from .models import User, ActivityLog, Car, UserCar

admin.site.register(User)
admin.site.register(Car)
admin.site.register(UserCar)
# admin.site.register(ActivityLog)

@admin.register(ActivityLog)
class ActivityLog(admin.ModelAdmin):
    list_display = ('user_car','get_time','return_time','travel_mileage')