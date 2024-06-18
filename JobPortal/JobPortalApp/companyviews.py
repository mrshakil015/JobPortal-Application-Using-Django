from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from JobPortalApp.views import dashboard
from JobPortalApp.models import *
from JobPortalApp.forms import *

def companyRegistration(request):
    if request.method == 'POST':
        companyname=request.POST.get('companyname')
        username=request.POST.get('username')
        companyemail=request.POST.get('companyemail')
        companylogo=request.FILES.get('companylogo')
        password=request.POST.get('password')
        confirmpassword=request.POST.get('confirmpassword')
        
        if password == confirmpassword:
            user = IonicJobUserModel.objects.create_user(
                username=username,
                email=companyemail,
                password=password,
                UserType='Employer',
            )
            user.save()
            
            EmployerModel.objects.create(
               IonicUser=user,
               CompanyName= companyname,
               CompanyLogo = companylogo,
            )
            return redirect('companyLogin')
            
    
    return render(request,'company/companyregistration.html')

def companyLogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username, password=password)
        if user:
            if user.UserType == 'Employer':
                login(request,user)
                messages.success(request, 'Successfully Login')
                return redirect('dashboard')
            else:
                messages.warning(request, 'Username and Password not valid.')
                return redirect('companyLogin')
        else:
            messages.warning(request, 'Username and Password not valid.')
            return redirect('companyLogin')
    
    return render(request,'company/companylogin.html')

@login_required
def addjob(request):
    if request.method == 'POST':
        current_user = request.user
        form = JobForm(request.POST)
        
        if form.is_valid():
            job = form.save(commit=False)
            job.PostedBy = current_user
            job.save()
            return redirect('dashboard')
    else:
        form = JobForm()
    context = {
        'form':form
    }
    return render(request,'company/addjob.html',context)

def joblist(request):
    current_user = request.user
    jobdata = JobInfoModel.objects.filter(PostedBy=current_user)
    context ={
        'jobdata':jobdata
    }
    return render(request,'company/joblist.html',context)