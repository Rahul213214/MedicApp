from django.shortcuts import render
from .forms import ImageForm, ImageFormdoc, DoctorPostForm
from django.contrib.auth.models import User
from .models import patient, doctor, Doctorpost

# Create your views here.
def patientprofile(request):
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    form = ImageForm()
    
    
    log_user = request.user
    patientdata= patient.objects.filter(user=log_user)
    post = Doctorpost.objects.filter(draft='True')

    return render(request,'profile/patient/profilep.html',{'loguser':log_user,'patients':patientdata, 'form':form, 'post':post}) 


def doctorprofile(request):
    if request.method == "POST":
        form = ImageFormdoc(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    form = ImageFormdoc()
    
    
    log_user = request.user
    doctordata= doctor.objects.filter(user=log_user)

    return render(request,'profile/doctor/profiled.html',{'loguser':log_user,'doctors':doctordata, 'form':form}) 


def addpost(request):
    # xyz=id
    if request.method == "POST":
        fm=DoctorPostForm(request.POST, request.FILES)
        if fm.is_valid():
            user = fm.cleaned_data['user']
            tit = fm.cleaned_data['title']
            img = fm.cleaned_data['image']
            cat = fm.cleaned_data['category']
            summ = fm.cleaned_data['summary']
            cont = fm.cleaned_data['content']
            reg = Doctorpost(user=user,title=tit,image=img,category=cat,summary=summ,content=cont)
            reg.save()
    else:
        fm=DoctorPostForm()

    log_user = request.user
    post = Doctorpost.objects.filter(user=log_user)
    return render(request, 'profile/doctor/addpost.html',{'data':fm, 'post':post})