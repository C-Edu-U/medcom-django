from django import forms
from .models import ClinicalHistory

class ClinicalHistoryForm(forms.ModelForm):
    class Meta:
        model = ClinicalHistory
        fields = ['patient', 'doctor', 'appointment', 'service', 'description', 'attachments']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }
