from django.db import models
from .patient import Patient
from .doctor import Doctor
from .appointment import Appointment

class MedicalRecord(models.Model):

    record_id = models.AutoField(primary_key=True)


    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,
        related_name="medical_records"
    )


    doctor = models.ForeignKey(
        Doctor,
        on_delete=models.CASCADE,
        related_name="medical_records"
    )


    appointment = models.OneToOneField(
        Appointment,
        on_delete=models.CASCADE,
        related_name="medical_record"
    )


    diagnosis = models.TextField()


    treatment = models.TextField()


    prescription = models.TextField()


    notes = models.TextField(
        blank=True,
        null=True
    )


    date_created = models.DateTimeField(
        auto_now_add=True
    )


    def __str__(self):
        return f"Medical Record - {self.patient}"
    
