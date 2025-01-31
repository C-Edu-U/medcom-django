from django.urls import path
from .views import patient_login, patient_dashboard, patient_profile_update
from appointments.views import patient_appointment_booking

urlpatterns = [
    path('login/', patient_login, name='patient_login'),
    path('dashboard/', patient_dashboard, name='patient_dashboard'),
    path('appointment/book/', patient_appointment_booking, name='patient_appointment_booking'),
    path('profile/edit/', patient_profile_update, name='patient_profile_update'),
]
