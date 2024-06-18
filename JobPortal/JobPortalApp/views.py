from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from JobPortalApp.models import *

# Create your views here.
def homePage(request):
    
    return render(request,'index.html')

def browsejobPage(request):
    
    
    return render(request,'browsejob.html')

def seekerRegistration(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        confirmpassword=request.POST.get('confirmpassword')
        resume=request.FILES.get('resume')
        
        if password == confirmpassword:
            user = IonicJobUserModel.objects.create_user(
                username=username,
                email=email,
                password=password,
                UserType='Seeker',
            )
            user.save()
            
            SeekerModel.objects.create(
                IonicUser=user,
                Name=name,
                Resume = resume,
                )
            return redirect('seekerLogin')
    return render(request,'registration.html')

def seekerLogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username, password=password)
        if user:
            login(request,user)
            return redirect('dashboard')
        else:
            return redirect('seekerLogin')
    return render(request,'login.html')

@login_required
def logoutPage(request):
    logout(request)
    return redirect('homePage')

@login_required
def dashboard(request):
    current_user = request.user
    current_userType = request.user.UserType
    
    if current_userType == 'Employer':
        userdata = EmployerModel.objects.get(IonicUser=current_user)
    else:
        userdata = SeekerModel.objects.get(IonicUser=current_user)
        
    return render(request,'dashboard.html',{'userdata':userdata})