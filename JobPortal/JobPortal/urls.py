from django.contrib import admin
from django.urls import path
from JobPortalApp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homePage,name="homePage"),
    path('browsejob/', browsejobPage,name="browsejobPage"),
    path('registrationPage/', registrationPage,name="registrationPage"),
]
