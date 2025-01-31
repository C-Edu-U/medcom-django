from django import forms
from .models import Patient
from people.models import Person  # Import Person

class PatientForm(forms.ModelForm):
    person = forms.ModelChoiceField(queryset=Person.objects.all(), label="Select Person")

    class Meta:
        model = Patient
        fields = ['person']
