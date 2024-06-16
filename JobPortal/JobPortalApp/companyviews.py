from django.shortcuts import render, redirect
from JobPortalApp.models import *

def companyRegistration(request):
    
    return render(request,'company/companyregistration.html')

def companyLogin(request):
    
    
    return render(request,'company/companylogin.html')