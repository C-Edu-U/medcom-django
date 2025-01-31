from django.shortcuts import render, get_object_or_404, redirect
from .models import Service
from .forms import ServiceForm

# List all services
def service_list(request):
    services = Service.objects.all()
    return render(request, 'services/service_list.html', {'services': services})

# Create a new service
def service_create(request):
    if request.method == "POST":
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('service_list')
    else:
        form = ServiceForm()
    return render(request, 'services/service_form.html', {'form': form})

# Edit a service
def service_update(request, service_id):
    service = get_object_or_404(Service, id=service_id)
    if request.method == "POST":
        form = ServiceForm(request.POST, instance=service)
        if form.is_valid():
            form.save()
            return redirect('service_list')
    else:
        form = ServiceForm(instance=service)
    return render(request, 'services/service_form.html', {'form': form})

# Delete a service
def service_delete(request, service_id):
    service = get_object_or_404(Service, id=service_id)
    if request.method == "POST":
        service.delete()
        return redirect('service_list')
    return render(request, 'services/service_confirm_delete.html', {'service': service})
