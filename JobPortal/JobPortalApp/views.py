from django.shortcuts import render,redirect
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
    
    
    return render(request,'login.html')