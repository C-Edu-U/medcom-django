from django.urls import path
from .views import clinical_history_list, clinical_history_create, clinical_history_update, clinical_history_delete

urlpatterns = [
    path('', clinical_history_list, name='clinical_history_list'),
    path('create/', clinical_history_create, name='clinical_history_create'),
    path('<int:history_id>/edit/', clinical_history_update, name='clinical_history_update'),
    path('<int:history_id>/delete/', clinical_history_delete, name='clinical_history_delete'),
]
