from django.contrib import admin
from .models import Doctor, Specialization, DoctorSpecialization

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
