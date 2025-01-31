from django.shortcuts import render, get_object_or_404, redirect
from .models import ClinicalHistory
from .forms import ClinicalHistoryForm

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
