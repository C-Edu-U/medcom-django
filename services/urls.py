from django.urls import path
from .views import service_list, service_create, service_update, service_delete

urlpatterns = [
    path('', service_list, name='service_list'),
    path('create/', service_create, name='service_create'),
    path('<int:service_id>/edit/', service_update, name='service_update'),
    path('<int:service_id>/delete/', service_delete, name='service_delete'),
]
