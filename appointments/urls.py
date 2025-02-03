from django.urls import path
from .views import multi_step_appointment, appointment_success, patient_appointment_booking, get_available_slots, get_available_services

urlpatterns = [
    path('create/', multi_step_appointment, name='multi_step_appointment'),
    path('success/', appointment_success, name='appointment_success'),
    path('book/', patient_appointment_booking, name='patient_appointment_booking'),
    path('get_available_slots/', get_available_slots, name='get_available_slots'),
    path('get_available_services/', get_available_services, name='get_available_services'),
]

