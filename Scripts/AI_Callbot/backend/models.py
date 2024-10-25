from django.db import models

# Create your models here.
class patient(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    age = models.IntegerField((""))
    symptoms = models.TextField()
    urgency = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Appointment(models.Model):
    patient = models.ForeignKey(patient, on_delete=models.CASCADE)
    date = models.DateTimeField()
    doctor = models.CharField(max_length=100)

class Doctor(models.Model):
    Reg_no = models.CharField( max_length=50)
    D_name = models.CharField(max_length=50)
    D_phone = models.CharField(max_length=50)
    D_Department = models.ForeignKey(patient, on_delete=models.CASCADE)
    D_qualification = models.CharField(max_length=50)
    D_specialisation = models.CharField(max_length=50)

    def __str__(self):
        return self.D_name

class Department(models.Model):
    Dept_name = models.CharField(max_length=50)
    Dept_D_no = models.IntegerField()
    Dept_head = models.CharField(max_length=50)
    