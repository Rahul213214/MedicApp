
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('patientprofile/', views.patientprofile, name="patientprofile"),
    path('doctorprofile/', views.doctorprofile, name="doctorprofile"),

    path('addpost/', views.addpost, name='addpost'),
    # path('addpost/<str:user>', views.addpost, name='addpost'),
]