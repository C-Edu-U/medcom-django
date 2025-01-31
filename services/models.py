from django.db import models
from doctors.models import Doctor, Specialization

class Service(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    doctors = models.ManyToManyField(Doctor, related_name="services")  # Link to doctors
    specializations = models.ManyToManyField(Specialization, related_name="services")  # Link to specializations

    def __str__(self):
        return self.name
