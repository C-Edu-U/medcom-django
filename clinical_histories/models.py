from django.db import models
from doctors.models import Doctor
from patients.models import Patient
from services.models import Service
from appointments.models import Appointment

class ClinicalHistory(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="clinical_histories")
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name="signed_histories")
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE, blank=True, null=True)
    service = models.ForeignKey(Service, on_delete=models.SET_NULL, null=True)
    description = models.TextField()
    date = models.DateField(auto_now_add=True)
    attachments = models.FileField(upload_to='clinical_histories/', blank=True, null=True)

    def __str__(self):
        return f"Clinical History for {self.patient.person.first_name} {self.patient.person.last_name} - {self.date}"
