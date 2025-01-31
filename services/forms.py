from django import forms
from .models import Service
from doctors.models import Doctor, Specialization

class ServiceForm(forms.ModelForm):
    doctors = forms.ModelMultipleChoiceField(queryset=Doctor.objects.all(), widget=forms.CheckboxSelectMultiple, required=False)
    specializations = forms.ModelMultipleChoiceField(queryset=Specialization.objects.all(), widget=forms.CheckboxSelectMultiple, required=False)

    class Meta:
        model = Service
        fields = ['name', 'description', 'price', 'doctors', 'specializations']
