from django.contrib import admin
from .models import MedicalRecord


@admin.register(MedicalRecord)
class MedicalRecordAdmin(admin.ModelAdmin):
    list_display = ('record_id', 'patient', 'doctor', 'date_created')
    search_fields = ('patient__first_name', 'patient__last_name', 'diagnosis')
    list_filter = ('doctor',)
