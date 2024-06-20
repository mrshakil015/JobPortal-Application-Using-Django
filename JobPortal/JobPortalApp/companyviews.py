from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
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
                return redirect('postedjob')
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
            return redirect('postedjob')
    else:
        form = JobForm()
    context = {
        'form':form
    }
    return render(request,'company/addjob.html',context)

@login_required
def editjob(request,myid):
    jobdata = get_object_or_404(JobInfoModel, id=myid)
    if request.method == 'POST':
        form = JobForm(request.POST, instance=jobdata)
        if form.is_valid():
            form.save()
            return redirect('postedjob')
    else:
        form = JobForm(instance=jobdata)
    context = {
        'form':form
    }
    return render(request,'company/editjob.html',context)

@login_required
def deletejob(request,myid):
    jobdata = get_object_or_404(JobInfoModel, id=myid)
    jobdata.delete()
    
    return redirect('postedjob')

@login_required
def postedjob(request):
    current_user = request.user
    jobdata = JobInfoModel.objects.filter(PostedBy=current_user)
    context ={
        'jobdata':jobdata
    }
    return render(request,'company/postedjob.html',context)