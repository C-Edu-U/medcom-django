from django.contrib import admin
from .models import Doctor, Specialization, DoctorSpecialization, DoctorSchedule

@admin.register(Specialization)
class SpecializationAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('person',)
    search_fields = ('person__first_name', 'person__last_name')

@admin.register(DoctorSpecialization)
class DoctorSpecializationAdmin(admin.ModelAdmin):
    list_display = ('doctor', 'specialization', 'graduation_date')
    search_fields = ('doctor__person__first_name', 'specialization__name')

@admin.register(DoctorSchedule)
class DoctorScheduleAdmin(admin.ModelAdmin):
    list_display = ('doctor', 'date', 'time', 'is_booked')
    list_filter = ('doctor', 'date', 'is_booked')
    search_fields = ('doctor__person__first_name', 'doctor__person__last_name', 'date')
    ordering = ('doctor', 'date', 'time')
    list_editable = ('is_booked',)  # Allow admins to mark slots as booked/unbooked from the list view

