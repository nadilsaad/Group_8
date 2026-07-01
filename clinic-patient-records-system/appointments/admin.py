from django.contrib import admin
from .models import Appointment


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('appointment_id', 'patient', 'doctor', 'appointment_date', 'status')
    list_filter = ('status', 'doctor')
    search_fields = ('patient__first_name', 'patient__last_name', 'doctor__last_name')
