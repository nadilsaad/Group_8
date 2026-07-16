from django.contrib import admin

# Register your models here.
from .models import Appointment, Bill, Doctor, Patient, MedicalRecord
admin.site.register(Appointment)
admin.site.register(Bill)
admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(MedicalRecord)