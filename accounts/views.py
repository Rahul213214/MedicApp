from django.shortcuts import render
from .forms import SignUpForm
from django.contrib import messages
from django.shortcuts import render, HttpResponseRedirect, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout

# Create your views here.
# Register patient
def registerPatient(request):
    form = SignUpForm()

    if request.method=="POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for '+user)
            return redirect('loginpatient')
    context={'form':form}
    return render(request, 'patient/registerp.html', context)


#Login Pateint

def loginPatient(request):
    if request.method=="POST":
        fm = AuthenticationForm(request=request, data=request.POST)
        if fm.is_valid():
            uname = fm.cleaned_data['username']
            upass = fm.cleaned_data['password']
            user=authenticate(username=uname, password=upass)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/app/patientprofile/')
            else:
                messages.info(request, "Username Or password is incorrect. ")
                # return render(request, 'login.html')
    else:
        fm=AuthenticationForm()

    fm=AuthenticationForm()
    return render(request, 'patient/loginp.html', {'form':fm})


# *****************************************************************************************************

def registerDoctor(request):
    form = SignUpForm()

    if request.method=="POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for '+user)
            return redirect('loginDoctor')
    context={'form':form}
    return render(request, 'doctor/registerd.html', context)



def loginDoctor(request):
    if request.method=="POST":
        fm = AuthenticationForm(request=request, data=request.POST)
        if fm.is_valid():
            uname = fm.cleaned_data['username']
            upass = fm.cleaned_data['password']
            user=authenticate(username=uname, password=upass)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/app/doctorprofile/')
            else:
                messages.info(request, "Username Or password is incorrect. ")
                # return render(request, 'login.html')
    else:
        fm=AuthenticationForm()

    fm=AuthenticationForm()
    return render(request, 'doctor/logind.html', {'form':fm})