from django.urls import path
from .views import reports_dashboard, generate_revenue_summary_pdf

urlpatterns = [
    path('', reports_dashboard, name='reports_dashboard'),
    path('generate_revenue_pdf/', generate_revenue_summary_pdf, name='generate_revenue_summary_pdf'),
]
