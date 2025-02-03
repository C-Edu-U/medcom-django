from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from django.db.models import Count, Sum
from appointments.models import Appointment
from doctors.models import Doctor
from patients.models import Patient
from services.models import Service
from datetime import datetime
from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from datetime import datetime

# Function to check if the user is a superuser
def is_superuser(user):
    return user.is_authenticated and user.is_superuser

@login_required  # Requires login
@user_passes_test(is_superuser)  # Restricts access to superusers only
def reports_dashboard(request):
    start_date = request.GET.get('start_date', '2023-01-01')
    end_date = request.GET.get('end_date', datetime.today().strftime('%Y-%m-%d'))

    total_patients = Patient.objects.count()
    total_doctors = Doctor.objects.count()
    total_services = Service.objects.count()
    total_appointments = Appointment.objects.filter(date__range=[start_date, end_date]).count()

    total_revenue = (
        Appointment.objects.filter(date__range=[start_date, end_date], status="Completed")
        .aggregate(Sum('service__price'))['service__price__sum'] or 0
    )

    appointments_by_status = (
        Appointment.objects.filter(date__range=[start_date, end_date])
        .values('status')
        .annotate(count=Count('status'))
        .order_by('-count')
    )

    appointments_by_doctor = (
        Appointment.objects.filter(date__range=[start_date, end_date])
        .values('doctor__person__first_name', 'doctor__person__last_name')
        .annotate(count=Count('doctor'))
        .order_by('-count')
    )

    appointments_by_service = (
        Appointment.objects.filter(date__range=[start_date, end_date])
        .values('service__name')
        .annotate(count=Count('service'))
        .order_by('-count')
    )

    revenue_by_month = (
        Appointment.objects.filter(date__range=[start_date, end_date], status="Completed")
        .values('date__year', 'date__month')
        .annotate(total_revenue=Sum('service__price'))
        .order_by('date__year', 'date__month')
    )

    revenue_labels = [f"{entry['date__year']}-{entry['date__month']:02d}" for entry in revenue_by_month]
    revenue_values = [entry['total_revenue'] if entry['total_revenue'] else 0 for entry in revenue_by_month]

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
            'total_revenue': total_revenue,
            'appointments_by_status': appointments_by_status,
            'appointments_by_doctor': appointments_by_doctor,
            'appointments_by_service': appointments_by_service,
            'revenue_labels': revenue_labels,
            'revenue_values': revenue_values,
        },
    )

@login_required
@user_passes_test(lambda u: u.is_superuser)  # Ensure only superusers can access
def generate_revenue_summary_pdf(request):
    start_date = request.GET.get('start_date', '2023-01-01')
    end_date = request.GET.get('end_date', datetime.today().strftime('%Y-%m-%d'))

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="revenue_summary_{start_date}_to_{end_date}.pdf"'

    # Create PDF document
    doc = SimpleDocTemplate(response, pagesize=letter)
    elements = []
    styles = getSampleStyleSheet()

    # Header
    elements.append(Paragraph("Revenue Summary Report", styles['Title']))
    elements.append(Paragraph(f"Date Range: {start_date} to {end_date}", styles['Normal']))
    elements.append(Spacer(1, 12))

    # Total Revenue
    total_revenue = (
        Appointment.objects.filter(date__range=[start_date, end_date], status="Completed")
        .aggregate(Sum('service__price'))['service__price__sum'] or 0
    )

    elements.append(Paragraph(f"Total Revenue: <b>${total_revenue:,.2f}</b>", styles['Heading2']))
    elements.append(Spacer(1, 12))

    # Monthly Revenue Breakdown
    elements.append(Paragraph("Revenue by Month", styles['Heading3']))
    revenue_by_month = (
        Appointment.objects.filter(date__range=[start_date, end_date], status="Completed")
        .values('date__year', 'date__month')
        .annotate(total_revenue=Sum('service__price'))
        .order_by('date__year', 'date__month')
    )

    month_table_data = [["Month", "Total Revenue"]]
    for entry in revenue_by_month:
        month_label = f"{entry['date__year']}-{entry['date__month']:02d}"
        revenue = entry['total_revenue'] or 0
        month_table_data.append([month_label, f"${revenue:,.2f}"])

    month_table = Table(month_table_data)
    month_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))
    elements.append(month_table)
    elements.append(Spacer(1, 12))

    # Revenue by Service
    elements.append(Paragraph("Revenue by Service", styles['Heading3']))
    revenue_by_service = (
        Appointment.objects.filter(date__range=[start_date, end_date], status="Completed")
        .values('service__name')
        .annotate(total_revenue=Sum('service__price'))
        .order_by('-total_revenue')
    )

    service_table_data = [["Service", "Total Revenue"]]
    for entry in revenue_by_service:
        service_name = entry['service__name'] if entry['service__name'] else "N/A"
        revenue = entry['total_revenue'] or 0
        service_table_data.append([service_name, f"${revenue:,.2f}"])

    service_table = Table(service_table_data)
    service_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))
    elements.append(service_table)
    elements.append(Spacer(1, 12))

    # Service History Table (Completed & Paid Appointments)
    elements.append(Paragraph("Service History (Completed & Paid)", styles['Heading3']))
    service_history = (
        Appointment.objects.filter(date__range=[start_date, end_date], status="Completed")
        .values('date', 'service__name', 'patient__person__first_name', 'patient__person__last_name', 'service__price')
        .order_by('-date')
    )

    service_history_table_data = [["Date", "Service", "Patient", "Price"]]
    for entry in service_history:
        date = entry['date'].strftime('%Y-%m-%d')
        service_name = entry['service__name'] if entry['service__name'] else "N/A"
        patient_name = f"{entry['patient__person__first_name']} {entry['patient__person__last_name']}"
        price = f"${entry['service__price']:,.2f}" if entry['service__price'] else "$0.00"
        service_history_table_data.append([date, service_name, patient_name, price])

    service_history_table = Table(service_history_table_data)
    service_history_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))
    elements.append(service_history_table)

    # Build PDF
    doc.build(elements)
    return response


