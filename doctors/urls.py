from django.urls import path
from .views import doctor_list, doctor_create, doctor_update, doctor_delete

urlpatterns = [
    path('', doctor_list, name='doctor_list'),
    path('create/', doctor_create, name='doctor_create'),
    path('<int:doctor_id>/edit/', doctor_update, name='doctor_update'),
    path('<int:doctor_id>/delete/', doctor_delete, name='doctor_delete'),
]
