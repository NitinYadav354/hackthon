from django.contrib import admin
from .models import patient ,Appointment, Doctor, Department

# Register your models here.
admin.site.register(Appointment)
admin.site.register(patient)
admin.site.register(Department)
admin.site.register(Doctor)