"""traffic_management URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from traffic_management_app import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('detection/', views.detection, name='detection'),
    path('status_of_signals/',views.status_of_signals, name='status_of_signals'),
    path('allocate_time/', views.allocate_time, name='allocate_time'),
    path('detect_plate/', views.detect_plate, name='detect_plate'),
    path('shortest_path/', views.shortest_path, name='shortest_path'),
]
