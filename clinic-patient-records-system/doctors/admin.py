from django.contrib import admin
from .models import Doctor


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('doctor_id', 'first_name', 'last_name', 'specialization', 'phone_number', 'email')
    search_fields = ('first_name', 'last_name', 'license_number', 'email')
    list_filter = ('specialization',)
