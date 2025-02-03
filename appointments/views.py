from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login
from patients.models import Patient
from people.models import Person
from .models import Appointment
from .forms import UserRegistrationForm, PersonForm
from django.contrib.auth.decorators import login_required
from appointments.forms import PatientAppointmentForm
from patients.models import Patient
from doctors.models import DoctorSchedule
from django.http import JsonResponse
from services.models import Service


def multi_step_registration(request):
    if request.method == "POST":
        user_form = UserRegistrationForm(request.POST)
        person_form = PersonForm(request.POST)

        if user_form.is_valid() and person_form.is_valid():
            # Step 1: Create the User
            user = user_form.save()
            login(request, user)  # Auto-login the user

            # Step 2: Create the Person linked to the user
            person = person_form.save()

            # Step 3: Create a Patient linked to the Person
            patient = Patient.objects.create(person=person)

            return redirect('registration_success')  # Redirect to success page
        
    else:
        user_form = UserRegistrationForm()
        person_form = PersonForm()

    return render(
        request,
        'appointments/multi_step_registration.html',
        {
            'user_form': user_form,
            'person_form': person_form
        }
    )

def registration_success(request):
    return render(request, 'appointments/registration_success.html')

@login_required
def patient_appointment_booking(request):
    # Ensure only patients can access
    if not request.user.groups.filter(name="Patients").exists():
        return redirect('patient_login')

    try:
        patient = Patient.objects.get(person__email=request.user.email)
    except Patient.DoesNotExist:
        return redirect('patient_dashboard')

    if request.method == "POST":
        form = PatientAppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.patient = patient  # Assign logged-in patient
            
            # Retrieve the selected time slot and mark it as booked
            time_slot = form.cleaned_data['time_slot']
            time_slot.is_booked = True
            time_slot.save()

            # Assign the booked slot to the appointment
            appointment.date = time_slot.date
            appointment.time = time_slot.time
            appointment.save()

            return redirect('patient_dashboard')
    else:
        form = PatientAppointmentForm()

    return render(request, 'appointments/patient_appointment_form.html', {'form': form})


def get_available_slots(request):
    doctor_id = request.GET.get('doctor_id')
    date = request.GET.get('date')
    slots = DoctorSchedule.objects.filter(doctor_id=doctor_id, date=date, is_booked=False).values('id', 'time')
    return JsonResponse(list(slots), safe=False)


def get_available_services(request):
    doctor_id = request.GET.get('doctor_id')

    if not doctor_id:
        return JsonResponse([], safe=False)

    # Get services where the selected doctor is assigned
    services = Service.objects.filter(doctors__id=doctor_id).values('id', 'name')

    return JsonResponse(list(services), safe=False)
