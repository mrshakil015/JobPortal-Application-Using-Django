from django.contrib import admin
from django.urls import path
from JobPortalApp.views import *
from JobPortalApp.companyviews import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homePage,name="homePage"),
    path('browsejob/', browsejobPage,name="browsejobPage"),
    path('seekerRegistration/', seekerRegistration,name="seekerRegistration"),
    path('seekerLogin/', seekerLogin,name="seekerLogin"),
    path('logout/', logoutPage, name='logout'),
    
    
    path('companyRegistration/', companyRegistration,name="companyRegistration"),
    path('companyLogin/', companyLogin,name="companyLogin"),
    
    path('dashboard/', dashboard,name="dashboard"),
    
    #--------------Job---------------
    path('addjob/', addjob,name="addjob"),
    path('postedjob/', postedjob,name="postedjob"),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
