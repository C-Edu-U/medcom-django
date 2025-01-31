from django.contrib import admin
from .models import Appointment

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('date', 'time', 'patient', 'doctor', 'service', 'status')
    search_fields = ('patient__person__first_name', 'doctor__person__first_name')
    list_filter = ('status', 'date')
