from django.shortcuts import render, redirect
from .models import Appointment, Department, Doctor, patient

def home(request):
    patient_count = patient.objects.count()
    app_count = Appointment.objects.count()
    doctor = Doctor.objects.all()
    app = Appointment.objects.all()
    return render(request, 'backend/index.html', {'patient_count':patient_count, 'app_count':app_count, 'doctor': doctor, 'app':app})