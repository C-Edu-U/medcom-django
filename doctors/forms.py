from django import forms
from .models import Doctor, Specialization, DoctorSpecialization
from patients.models import Person

class DoctorForm(forms.ModelForm):
    person = forms.ModelChoiceField(queryset=Person.objects.all(), label="Select Person")

    class Meta:
        model = Doctor
        fields = ['person']

class SpecializationForm(forms.ModelForm):
    class Meta:
        model = Specialization
        fields = ['name', 'description']

class DoctorSpecializationForm(forms.ModelForm):
    class Meta:
        model = DoctorSpecialization
        fields = ['doctor', 'specialization', 'graduation_date']
        widgets = {
            'graduation_date': forms.DateInput(attrs={'type': 'date'})
        }
