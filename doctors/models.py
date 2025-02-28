from django.db import models
from patients.models import Person

class Specialization(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Doctor(models.Model):
    person = models.OneToOneField(Person, on_delete=models.CASCADE)  # Each doctor is a person
    specializations = models.ManyToManyField(Specialization, through="DoctorSpecialization")

    def __str__(self):
        return f"Dr. {self.person.first_name} {self.person.last_name}"

class DoctorSpecialization(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    specialization = models.ForeignKey(Specialization, on_delete=models.CASCADE)
    graduation_date = models.DateField()

    def __str__(self):
        return f"{self.doctor} - {self.specialization.name}"

class DoctorSchedule(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name="schedules")
    date = models.DateField()  # The day the doctor is available
    time = models.TimeField()  # The specific available time slot
    is_booked = models.BooleanField(default=False)  # Marks if the slot is taken

    def __str__(self):
        return f"{self.doctor.person.first_name} - {self.date} at {self.time}"