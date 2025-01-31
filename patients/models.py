from django.db import models
from people.models import Person  # Import from the new people app

class Patient(models.Model):
    person = models.OneToOneField(Person, on_delete=models.CASCADE)

    def __str__(self):
        return f"Patient: {self.person.first_name} {self.person.last_name}"

