from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from appointments.models import Appointment
from .forms import PatientLoginForm
from patients.models import Patient
from django.contrib.auth.models import User
from patients.models import Patient
from people.models import Person
from .forms import UserUpdateForm, PersonUpdateForm

def patient_login(request):
    if request.method == "POST":
        form = PatientLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            # Ensure user belongs to the Patients group
            if user.groups.filter(name="Patients").exists():
                login(request, user)
                return redirect('patient_dashboard')
            else:
                form.add_error(None, "You do not have permission to access this area.")
    else:
        form = PatientLoginForm()

    return render(request, 'patients/patient_login.html', {'form': form})

@login_required
def patient_dashboard(request):
    # Ensure only patients can access
    if not request.user.groups.filter(name="Patients").exists():
        return redirect('patient_login')

    # Get the associated patient object
    try:
        patient = Patient.objects.get(person__email=request.user.email)
    except Patient.DoesNotExist:
        return redirect('patient_login')

    # Fetch only the logged-in patient's appointments
    appointments = Appointment.objects.filter(patient=patient).order_by('-date')

    return render(request, 'patients/patient_dashboard.html', {
        'patient': patient,
        'appointments': appointments
    })

@login_required
def patient_profile_update(request):
    # Ensure only patients can access
    if not request.user.groups.filter(name="Patients").exists():
        return redirect('patient_login')

    try:
        patient = Patient.objects.get(person__email=request.user.email)
    except Patient.DoesNotExist:
        return redirect('patient_dashboard')

    user_form = UserUpdateForm(instance=request.user)
    person_form = PersonUpdateForm(instance=patient.person)

    if request.method == "POST":
        user_form = UserUpdateForm(request.POST, instance=request.user)
        person_form = PersonUpdateForm(request.POST, instance=patient.person)

        if user_form.is_valid() and person_form.is_valid():
            user_form.save()
            person_form.save()
            return redirect('patient_dashboard')

    return render(request, 'patients/patient_profile_update.html', {
        'user_form': user_form,
        'person_form': person_form
    })
