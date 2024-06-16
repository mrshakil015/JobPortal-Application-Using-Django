from django.db import models
from django.contrib.auth.models import AbstractUser

class IonicJobUserModel(AbstractUser):
    USERTYPE = [
        ('Employer','Employer'),
        ('Seeker','Seeker'),
    ]
    UserType = models.CharField(choices=USERTYPE,max_length=50, null=True)
    
    class Meta:
        db_table = 'IonicJob_User_Table'

class EmployerModel(models.Model):
    CompanyName = models.CharField(max_length=100, null=True)
    CompanyAddress = models.CharField(max_length=100, null=True)
    Mobile = models.CharField(max_length=100, null=True)
    CompanyLogo = models.ImageField(upload_to='media/companylogo',null=True)
    IonicUser = models.OneToOneField(IonicJobUserModel, on_delete=models.CASCADE, related_name='employeermodel',null=True)
    
    class Meta:
        db_table = 'Employer_Table'

class SeekerModel(models.Model):
    Name = models.CharField(max_length=100, null=True)
    Address = models.CharField(max_length=100, null=True)
    Mobile = models.CharField(max_length=100, null=True)
    DateOfBirth = models.DateField(null=True)
    ProfileImg = models.ImageField(upload_to='media/seekerImage',null=True)
    Resume = models.FileField(upload_to='media/seekerResume',null=True)
    IonicUser = models.OneToOneField(IonicJobUserModel, on_delete=models.CASCADE, related_name='seekermodel',null=True)
    
    class Meta:
        db_table = 'JobSeeker_Table'
    
    

