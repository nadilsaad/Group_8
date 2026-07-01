from django.db import models


class Doctor(models.Model):
    SPECIALIZATION_CHOICES = [
        ('GEN', 'General Practitioner'),
        ('PED', 'Pediatrician'),
        ('DENT', 'Dentist'),
        ('DERM', 'Dermatologist'),
        ('GYN', 'Gynecologist'),
        ('OPT', 'Ophthalmologist'),
        ('OTHER', 'Other'),
    ]

    doctor_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    specialization = models.CharField(max_length=10, choices=SPECIALIZATION_CHOICES, default='GEN')
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    license_number = models.CharField(max_length=30, unique=True)
    date_joined = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['last_name', 'first_name']

    def __str__(self):
        return f"Dr. {self.first_name} {self.last_name} ({self.get_specialization_display()})"
