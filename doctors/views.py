from django.shortcuts import render, get_object_or_404, redirect
from .models import Doctor, Specialization, DoctorSpecialization
from .forms import DoctorForm, SpecializationForm, DoctorSpecializationForm

# List all doctors
def doctor_list(request):
    doctors = Doctor.objects.all()
    return render(request, 'doctors/doctor_list.html', {'doctors': doctors})

# Add a new doctor
def doctor_create(request):
    if request.method == "POST":
        form = DoctorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('doctor_list')
    else:
        form = DoctorForm()
    return render(request, 'doctors/doctor_form.html', {'form': form})

# Edit an existing doctor
def doctor_update(request, doctor_id):
    doctor = get_object_or_404(Doctor, id=doctor_id)
    if request.method == "POST":
        form = DoctorForm(request.POST, instance=doctor)
        if form.is_valid():
            form.save()
            return redirect('doctor_list')
    else:
        form = DoctorForm(instance=doctor)
    return render(request, 'doctors/doctor_form.html', {'form': form})

# Delete a doctor
def doctor_delete(request, doctor_id):
    doctor = get_object_or_404(Doctor, id=doctor_id)
    if request.method == "POST":
        doctor.delete()
        return redirect('doctor_list')
    return render(request, 'doctors/doctor_confirm_delete.html', {'doctor': doctor})
