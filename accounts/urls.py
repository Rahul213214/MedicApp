
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('patientr/', views.registerPatient, name="registerpatient"),
    path('patientl/', views.loginPatient, name="loginpatient"),

    path('doctorr/', views.registerDoctor, name="registerDoctor"),
    path('doctorl/', views.loginDoctor, name="loginDoctor"),


]
