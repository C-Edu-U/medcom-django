from django.urls import path
from .views import appointment_list, appointment_create, appointment_update, appointment_delete

urlpatterns = [
    path('', appointment_list, name='appointment_list'),
    path('create/', appointment_create, name='appointment_create'),
    path('<int:appointment_id>/edit/', appointment_update, name='appointment_update'),
    path('<int:appointment_id>/delete/', appointment_delete, name='appointment_delete'),
]
