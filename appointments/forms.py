from django import forms
from django.contrib.auth.models import User, Group
from patients.models import Patient
from people.models import Person
from appointments.models import Appointment
from doctors.models import Doctor
from services.models import Service
from doctors.models import DoctorSchedule

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
    date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        required=True
    )

    service = forms.ModelChoiceField(
        queryset=Service.objects.none(),  # Start empty, dynamically updated
        empty_label="Select Service",
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    time_slot = forms.ModelChoiceField(
        queryset=DoctorSchedule.objects.none(),  # Start empty, dynamically updated
        empty_label="Select Available Time",
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Appointment
        fields = ['date', 'doctor', 'service', 'time_slot']
        widgets = {
            'doctor': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(PatientAppointmentForm, self).__init__(*args, **kwargs)

        if 'doctor' in self.data:
            try:
                doctor_id = int(self.data.get('doctor'))
                self.fields['service'].queryset = Service.objects.filter(doctors__id=doctor_id)
            except (ValueError, TypeError):
                pass

        if 'doctor' in self.data and 'date' in self.data:
            try:
                doctor_id = int(self.data.get('doctor'))
                selected_date = self.data.get('date')
                self.fields['time_slot'].queryset = DoctorSchedule.objects.filter(
                    doctor_id=doctor_id,
                    date=selected_date,
                    is_booked=False
                )
            except (ValueError, TypeError):
                pass