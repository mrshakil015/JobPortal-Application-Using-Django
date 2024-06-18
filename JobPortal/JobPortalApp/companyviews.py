from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from JobPortalApp.views import dashboard
from JobPortalApp.models import *

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
            login(request,user)
            return redirect('dashboard')
        else:
            return redirect('companyLogin')
    
    return render(request,'company/companylogin.html')

