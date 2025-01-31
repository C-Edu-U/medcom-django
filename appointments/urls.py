from django.urls import path
from .views import multi_step_appointment, appointment_success

urlpatterns = [
    path('create/', multi_step_appointment, name='multi_step_appointment'),
    path('success/', appointment_success, name='appointment_success'),
]

