
from django.contrib import admin
from app.models import patient, doctor, Doctorpost
# Register your models here.
@admin.register(patient)
class PatientAdmin(admin.ModelAdmin):
    list_display=['user', 'picture', 'address']


@admin.register(doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display=['user', 'picture', 'address']

@admin.register(Doctorpost)
class DoctorPostAdmin(admin.ModelAdmin):
    list_display=['user','title', 'image', 'category', 'summary','content', 'draft']