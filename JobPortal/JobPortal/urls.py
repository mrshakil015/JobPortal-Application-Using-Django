from django.contrib import admin
from django.urls import path
from JobPortalApp.views import *
from JobPortalApp.companyviews import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homePage,name="homePage"),
    path('browsejob/', browsejobPage,name="browsejobPage"),
    path('seekerRegistration/', seekerRegistration,name="seekerRegistration"),
    path('seekerLogin/', seekerLogin,name="seekerLogin"),
    
    
    path('companyRegistration/', companyRegistration,name="companyRegistration"),
    path('companyLogin/', companyLogin,name="companyLogin"),
]
