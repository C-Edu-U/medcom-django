from django.urls import path
from .views import multi_step_registration, registration_success, patient_appointment_booking, get_available_slots, get_available_services

urlpatterns = [
    path('register/', multi_step_registration, name='multi_step_registration'),
    path('success/', registration_success, name='registration_success'),
    path('book/', patient_appointment_booking, name='patient_appointment_booking'),
    path('get_available_slots/', get_available_slots, name='get_available_slots'),
    path('get_available_services/', get_available_services, name='get_available_services'),
]

