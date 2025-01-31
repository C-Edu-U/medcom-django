from django.shortcuts import render
from django.db.models import Count
from appointments.models import Appointment
from doctors.models import Doctor
from patients.models import Patient
from services.models import Service

def reports_dashboard(request):
    # Get date range filter from request (default: last 30 days)
    start_date = request.GET.get('start_date', '2023-01-01')
    end_date = request.GET.get('end_date', '2030-12-31')

    # Count all registered records
    total_patients = Patient.objects.count()
    total_doctors = Doctor.objects.count()
    total_services = Service.objects.count()
    total_appointments = Appointment.objects.filter(date__range=[start_date, end_date]).count()

    # Group appointments by status
    appointments_by_status = (
        Appointment.objects.filter(date__range=[start_date, end_date])
        .values('status')
        .annotate(count=Count('status'))
        .order_by('-count')
    )

    # Group appointments by doctor
    appointments_by_doctor = (
        Appointment.objects.filter(date__range=[start_date, end_date])
        .values('doctor__person__first_name', 'doctor__person__last_name')
        .annotate(count=Count('doctor'))
        .order_by('-count')
    )

    # Group appointments by service
    appointments_by_service = (
        Appointment.objects.filter(date__range=[start_date, end_date])
        .values('service__name')
        .annotate(count=Count('service'))
        .order_by('-count')
    )

    return render(
        request,
        'reports/reports_dashboard.html',
        {
            'start_date': start_date,
            'end_date': end_date,
            'total_patients': total_patients,
            'total_doctors': total_doctors,
            'total_services': total_services,
            'total_appointments': total_appointments,
            'appointments_by_status': appointments_by_status,
            'appointments_by_doctor': appointments_by_doctor,
            'appointments_by_service': appointments_by_service,
        },
    )


