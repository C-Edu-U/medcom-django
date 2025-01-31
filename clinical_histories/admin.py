from django.contrib import admin
from .models import ClinicalHistory

@admin.register(ClinicalHistory)
class ClinicalHistoryAdmin(admin.ModelAdmin):
    list_display = ('date', 'patient', 'doctor', 'service', 'appointment')
    search_fields = ('patient__person__first_name', 'doctor__person__first_name')
    list_filter = ('date',)
