from django.db import models
from clinic.models.patient import Patient
from clinic.models.doctor import Doctor

class Appointment(models.Model):

    appointment_id = models.AutoField(primary_key=True)


    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,
        related_name="appointments"
    )


    doctor = models.ForeignKey(
        Doctor,
        on_delete=models.CASCADE,
        related_name="appointments"
    )


    appointment_date = models.DateTimeField()


    reason = models.TextField()


    status_choices = [
        ('Pending','Pending'),
        ('Completed','Completed'),
        ('Cancelled','Cancelled'),
    ]


    status = models.CharField(
        max_length=20,
        choices=status_choices,
        default='Pending'
    )


    created_at = models.DateTimeField(
        auto_now_add=True
    )


    def __str__(self):
        return f"{self.patient} - {self.appointment_date}"
