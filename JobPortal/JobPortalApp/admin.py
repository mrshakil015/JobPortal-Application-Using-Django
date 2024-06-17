from django.contrib import admin
from JobPortalApp.models import *
# Register your models here.
class UserDisplay(admin.ModelAdmin):
    list_display=['username','email','UserType']
admin.site.register(IonicJobUserModel,UserDisplay)

class EmployerDisplay(admin.ModelAdmin):
    list_display=['CompanyName','IonicUser']
admin.site.register(EmployerModel,EmployerDisplay)

class SeekerDisplay(admin.ModelAdmin):
    list_display=['Name','IonicUser']
admin.site.register(SeekerModel,SeekerDisplay)

class QualificationDisplay(admin.ModelAdmin):
    list_display=['DegreeName','IonicUser']
admin.site.register(QualificationModel,QualificationDisplay)

class WorkDisplay(admin.ModelAdmin):
    list_display=['Designation','IonicUser']
admin.site.register(WorkExperienceModel,WorkDisplay)

class JobDisplay(admin.ModelAdmin):
    list_display=['JobTitle','CompanyName','PostedBy']
admin.site.register(JobInfoModel,JobDisplay)

class ApplicantDisplay(admin.ModelAdmin):
    list_display=['Applicant','Job']
admin.site.register(JobApplicantModel,ApplicantDisplay)



