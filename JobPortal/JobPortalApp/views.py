from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from JobPortalApp.models import *
from django.contrib import messages

# Create your views here.
def homePage(request):
    
    return render(request,'index.html')

def browsejobPage(request):
    jobdata = JobInfoModel.objects.all()
    context ={
        'jobdata':jobdata
    }    
    return render(request,'jobinfo/browsejob.html',context)

def viewjob(request,myid):
    jobdata = get_object_or_404(JobInfoModel, id=myid)
    
    context = {
        'jobdata':jobdata
    }
    
    return render(request,'jobinfo/viewjob.html',context)

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
        
        user = authenticate(username=username, password=password,UserType='Seeker')
        if user:
            if user.UserType == 'Seeker':
                login(request,user)
                messages.success(request, 'Successfully Login')
                return redirect('dashboard')
            else:
                messages.warning(request, 'Username and Password not valid.')
                return redirect('seekerLogin')
        else:
            messages.warning(request, 'Username and Password not valid.')
            return redirect('seekerLogin')
    return render(request,'login.html')

@login_required
def logoutPage(request):
    logout(request)
    messages.warning(request, '')
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