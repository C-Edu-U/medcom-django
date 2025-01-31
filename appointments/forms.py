from django import forms
from django.contrib.auth.models import User, Group
from patients.models import Patient
from people.models import Person
from appointments.models import Appointment
from doctors.models import Doctor
from services.models import Service

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])  # Hash password
        if commit:
            user.save()
            patient_group, created = Group.objects.get_or_create(name="Patients")  # Ensure Patients group exists
            user.groups.add(patient_group)  # Add user to the Patients group
        return user

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'date_of_birth', 'email', 'phone', 'address', 'gender']

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['date', 'time', 'doctor', 'service']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
        }

class PatientAppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['date', 'time', 'doctor', 'service']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
        }