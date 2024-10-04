from django.db import models


class Patient(models.Model):
    name = models.CharField(max_length=100, default='John Doe')
    age = models.IntegerField(default=30)
    gender = models.CharField(max_length=10, default='Male')
    # address = models.CharField(max_length=255, default='123 Main St')
    contact_number = models.CharField(max_length=15, default='1234567890')
    diagnosis = models.CharField(max_length=255, default='Not Diagnosed')

    def __str__(self):
        return f"{self.name} - {self.diagnosis}"
