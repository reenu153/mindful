from django.contrib import admin
from .models import PatientData, SleepData
# Register your models here.

admin.site.register(PatientData)
admin.site.register(SleepData)