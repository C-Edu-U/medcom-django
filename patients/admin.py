from django.contrib import admin
from .models import Patient

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('person',)
    search_fields = ('person__first_name', 'person__last_name')
