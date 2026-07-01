from django.contrib import admin
from .models import Patient


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('patient_id', 'first_name', 'last_name', 'gender', 'date_of_birth', 'phone_number', 'blood_group')
    search_fields = ('first_name', 'last_name', 'phone_number', 'email')
    list_filter = ('gender', 'blood_group')
