"""
URL configuration for medcom project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import redirect
from .views import start_page

# Redirect superusers to the reports page from admin
def admin_home(request):
    if request.user.is_superuser:
        return redirect('reports_dashboard')
    return redirect('admin:index')

urlpatterns = [
    path('', start_page, name='start_page'),  # Start page at the root URL
    path('admin/', admin.site.urls),
    path('persons/', include('people.urls')),
    path('patients/', include('patients.urls')),
    path('doctors/', include('doctors.urls')),
    path('services/', include('services.urls')),
    path('appointments/', include('appointments.urls')),
    path('clinical_histories/', include('clinical_histories.urls')),
    path('reports/', include('reports.urls')),
    path('clinical_histories/', include('clinical_histories.urls')),
    path('reports/', include('reports.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # Enable media file serving


