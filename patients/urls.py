from django.urls import path
from .views import patient_list, patient_create, patient_update, patient_delete

urlpatterns = [
    path('', patient_list, name='patient_list'),
    path('create/', patient_create, name='patient_create'),
    path('<int:patient_id>/edit/', patient_update, name='patient_update'),
    path('<int:patient_id>/delete/', patient_delete, name='patient_delete'),
]
