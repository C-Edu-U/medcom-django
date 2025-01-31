from django import forms
from .models import Appointment
from doctors.models import Doctor
from patients.models import Patient
from services.models import Service

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['date', 'time', 'patient', 'doctor', 'service', 'status']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
            'status': forms.Select()
        }
