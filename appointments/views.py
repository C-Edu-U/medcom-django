from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login
from patients.models import Patient
from people.models import Person
from .models import Appointment
from .forms import UserRegistrationForm, PersonForm, AppointmentForm
from django.contrib.auth.decorators import login_required
from appointments.models import Appointment
from appointments.forms import PatientAppointmentForm
from patients.models import Patient

def multi_step_appointment(request):
    if request.method == "POST":
        user_form = UserRegistrationForm(request.POST)
        person_form = PersonForm(request.POST)
        appointment_form = AppointmentForm(request.POST)

        if user_form.is_valid() and person_form.is_valid() and appointment_form.is_valid():
            # Step 1: Create the User
            user = user_form.save()
            login(request, user)  # Auto-login the user

            # Step 2: Create the Person linked to the user
            person = person_form.save()

            # Step 3: Create a Patient linked to the Person
            patient = Patient.objects.create(person=person)

            # Step 4: Create the Appointment linked to the Patient
            appointment = appointment_form.save(commit=False)
            appointment.patient = patient  # Link appointment to newly created patient
            appointment.save()

            return redirect('appointment_success')  # Redirect to success page
        
    else:
        user_form = UserRegistrationForm()
        person_form = PersonForm()
        appointment_form = AppointmentForm()

    return render(
        request,
        'appointments/multi_step_appointment.html',
        {
            'user_form': user_form,
            'person_form': person_form,
            'appointment_form': appointment_form
        }
    )

def appointment_success(request):
    return render(request, 'appointments/appointment_success.html')

@login_required
def patient_appointment_booking(request):
    # Ensure only patients can access
    if not request.user.groups.filter(name="Patients").exists():
        return redirect('patient_login')

    # Get the patient object linked to the logged-in user
    try:
        patient = Patient.objects.get(person__email=request.user.email)
    except Patient.DoesNotExist:
        return redirect('patient_dashboard')

    if request.method == "POST":
        form = PatientAppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.patient = patient  # Assign logged-in patient
            appointment.save()
            return redirect('patient_dashboard')
    else:
        form = PatientAppointmentForm()

    return render(request, 'appointments/patient_appointment_form.html', {'form': form})
