from django.contrib import admin
from JobPortalApp.models import *
# Register your models here.
class UserDisplay(admin.ModelAdmin):
    list_display=['username','email','UserType']
admin.site.register(IonicJobUserModel,UserDisplay)

class SeekerDisplay(admin.ModelAdmin):
    list_display=['Name','IonicUser']
admin.site.register(SeekerModel,SeekerDisplay)
