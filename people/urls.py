from django.urls import path
from .views import person_list, person_create, person_update, person_delete

urlpatterns = [
    path('', person_list, name='person_list'),
    path('create/', person_create, name='person_create'),
    path('<int:person_id>/edit/', person_update, name='person_update'),
    path('<int:person_id>/delete/', person_delete, name='person_delete'),
]
