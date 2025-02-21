"""
URL configuration for filmsweb project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from . import views


urlpatterns = [
    path('admin/', views.adminpage),
    path('',views.home),
    path('adminlog/',views.admin),
    path('home/',views.adminpage),
    path('allfilms/',views.allfilms),
    path('addfilmform/',views.addFilmsform),
    path('reqfilm/',views.addfilmdata),
    path('searchlang/',views.searchlangform),
    path('slang/<str:lang>/',views.searchlang),
    path('searchgen/',views.searchgenform),
    path('sgen/<str:gen>/',views.searchgen),
    path('uprating/',views.updaterating),
    path('upratestat/',views.updateratingstat),
    path('delfilmform/',views.delfilmform),
    path('delfilmstat/',views.donedeletefilm)
]
