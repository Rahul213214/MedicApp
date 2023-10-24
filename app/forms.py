from django import forms
from .models import patient, doctor, Doctorpost


class ImageForm(forms.ModelForm):
    class Meta:
        model = patient
        fields = '__all__'
    
class ImageFormdoc(forms.ModelForm):
    class Meta:
        model = doctor
        fields = '__all__'


class DoctorPostForm(forms.ModelForm):
    class Meta:
        model=Doctorpost
        # fields=['user','title', 'image', 'category', 'summary','content']
        fields='__all__'