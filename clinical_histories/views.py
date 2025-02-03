from django.shortcuts import render, get_object_or_404, redirect
from .models import ClinicalHistory
from .forms import ClinicalHistoryForm
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from patients.models import Patient

# List all clinical histories
def clinical_history_list(request):
    histories = ClinicalHistory.objects.all()
    return render(request, 'clinical_histories/clinical_history_list.html', {'histories': histories})

# Create a new clinical history
def clinical_history_create(request):
    if request.method == "POST":
        form = ClinicalHistoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('clinical_history_list')
    else:
        form = ClinicalHistoryForm()
    return render(request, 'clinical_histories/clinical_history_form.html', {'form': form})

# Edit a clinical history
def clinical_history_update(request, history_id):
    history = get_object_or_404(ClinicalHistory, id=history_id)
    if request.method == "POST":
        form = ClinicalHistoryForm(request.POST, request.FILES, instance=history)
        if form.is_valid():
            form.save()
            return redirect('clinical_history_list')
    else:
        form = ClinicalHistoryForm(instance=history)
    return render(request, 'clinical_histories/clinical_history_form.html', {'form': form})

# Delete a clinical history
def clinical_history_delete(request, history_id):
    history = get_object_or_404(ClinicalHistory, id=history_id)
    if request.method == "POST":
        history.delete()
        return redirect('clinical_history_list')
    return render(request, 'clinical_histories/clinical_history_confirm_delete.html', {'history': history})

@login_required
def generate_clinical_history_pdf(request):
    # Ensure the logged-in user is a patient
    try:
        patient = Patient.objects.get(person__email=request.user.email)
    except Patient.DoesNotExist:
        return HttpResponse("You are not authorized to view this page.", status=403)

    # Get the patient's clinical histories
    histories = ClinicalHistory.objects.filter(patient=patient)

    # Create the PDF response
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="clinical_histories.pdf"'

    # Create the PDF
    pdf = canvas.Canvas(response, pagesize=letter)
    pdf.setTitle("Clinical Histories Report")

    # Header
    pdf.setFont("Helvetica-Bold", 16)
    pdf.drawString(200, 750, "Clinical Histories Report")
    pdf.setFont("Helvetica", 12)
    pdf.drawString(50, 730, f"Patient: {patient.person.first_name} {patient.person.last_name}")

    # Table headers
    pdf.setFont("Helvetica-Bold", 10)
    pdf.drawString(50, 700, "Date")
    pdf.drawString(150, 700, "Doctor")
    pdf.drawString(300, 700, "Service")
    pdf.drawString(450, 700, "Notes")

    y_position = 680
    pdf.setFont("Helvetica", 10)

    # Add each clinical history to the PDF
    for history in histories:
        pdf.drawString(50, y_position, str(history.date))
        pdf.drawString(150, y_position, f"Dr. {history.doctor.person.first_name} {history.doctor.person.last_name}")
        pdf.drawString(300, y_position, history.service.name if history.service else "N/A")
        pdf.drawString(450, y_position, history.description[:40] + "..." if len(history.description) > 40 else history.description)
        y_position -= 20

        # Check if we need a new page
        if y_position < 50:
            pdf.showPage()
            pdf.setFont("Helvetica", 10)
            y_position = 750

    pdf.showPage()
    pdf.save()

    return response