from django.shortcuts import render, get_object_or_404, redirect
from .models import Person
from .forms import PersonForm

def person_list(request):
    persons = Person.objects.all()
    return render(request, 'people/person_list.html', {'persons': persons})

def person_create(request):
    if request.method == "POST":
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('person_list')
    else:
        form = PersonForm()
    return render(request, 'people/person_form.html', {'form': form})

def person_update(request, person_id):
    person = get_object_or_404(Person, id=person_id)
    if request.method == "POST":
        form = PersonForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            return redirect('person_list')
    else:
        form = PersonForm(instance=person)
    return render(request, 'people/person_form.html', {'form': form})

def person_delete(request, person_id):
    person = get_object_or_404(Person, id=person_id)
    if request.method == "POST":
        person.delete()
        return redirect('person_list')
    return render(request, 'people/person_confirm_delete.html', {'person': person})
