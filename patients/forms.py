from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from people.models import Person

class PatientLoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']

class PersonUpdateForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'date_of_birth', 'phone', 'address', 'gender']
