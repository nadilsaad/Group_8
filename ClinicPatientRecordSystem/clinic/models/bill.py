from django.db import models
class Bill(models.Model):
    CHOICES = [
        ('pending', 'Pending'),
        ('paid', 'Paid')
        
    ]
    bill_id = models.AutoField(primary_key=True)
    patient_id = models.ForeignKey('patient', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateField(null=True, blank=True)
    payment_status = models.CharField(max_length=20, choices=CHOICES, default='Pending')
    
    