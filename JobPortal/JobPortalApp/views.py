from django.shortcuts import render

# Create your views here.
def homePage(request):
    
    return render(request,'index.html')

def browsejobPage(request):
    
    
    return render(request,'browsejob.html')

def seekerRegistration(request):
    
    
    return render(request,'registration.html')

def seekerLogin(request):
    
    
    return render(request,'login.html')