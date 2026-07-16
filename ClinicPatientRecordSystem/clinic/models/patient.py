from django.db import models


class Patient(models.Model):
    patient_id = models.AutoField(primary_key=True)

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    date_of_birth = models.DateField()

    gender_choices = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]

    gender = models.CharField(
        max_length=10,
        choices=gender_choices
    )

    phone_number = models.CharField(
        max_length=20,
        unique=True
    )

    email = models.EmailField(
        unique=True
    )

    address = models.TextField()

    blood_group = models.CharField(
        max_length=5
    )

    emergency_contact_name = models.CharField(
        max_length=100
    )

    emergency_contact_phone = models.CharField(
        max_length=20
    )

    registered_on = models.DateTimeField(
        auto_now_add=True
    )


    def __str__(self):
        return f"{self.first_name} {self.last_name}"