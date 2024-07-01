from django.contrib import admin
from .models import User, ActivityLog, Car

admin.site.register(User)
admin.site.register(Car)
# admin.site.register(ActivityLog)

@admin.register(ActivityLog)
class ActivityLog(admin.ModelAdmin):
    list_display = ('car','get_time','return_time','travel_mileage')