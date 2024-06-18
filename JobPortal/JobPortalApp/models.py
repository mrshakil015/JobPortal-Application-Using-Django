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
    CompanyDescription = models.TextField(null=True)
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
    LastDegree= models.CharField(max_length=100,null=True)
    LinkedIn= models.CharField(max_length=100,null=True)
    GitHub= models.CharField(max_length=100,null=True)
    IonicUser = models.OneToOneField(IonicJobUserModel, on_delete=models.CASCADE, related_name='seekermodel',null=True)
    
    class Meta:
        db_table = 'JobSeeker_Table'
        
class QualificationModel(models.Model):
    IonicUser = models.ForeignKey(IonicJobUserModel,on_delete=models.CASCADE, related_name='qualification',null=True)
    DegreeName = models.CharField(max_length=100,null=True)
    InstituteName = models.CharField(max_length=100,null=True)
    Department = models.CharField(max_length=100,null=True)
    PassingYear = models.CharField(max_length=100,null=True)
    Grade = models.CharField(max_length=100,null=True)
    
    class Meta:
        db_table = 'Qualification_Table'

class WorkExperienceModel(models.Model):
    IonicUser = models.ForeignKey(IonicJobUserModel,on_delete=models.CASCADE, related_name='workexperience',null=True)
    Designation = models.CharField(max_length=100,null=True)
    InstituteName = models.CharField(max_length=100,null=True)
    Duration = models.CharField(max_length=100,null=True)
    
    class Meta:
        db_table = 'WorkExperience_Table'
    
class JobInfoModel(models.Model):
    JobTitle = models.CharField(max_length=100, null=True)
    JobDescription = models.TextField(null=True)
    Qualification = models.CharField(max_length=100, null=True)
    Salary = models.CharField(max_length=100, null=True)
    Deadline = models.CharField(max_length=100, null=True)
    Designation = models.CharField(max_length=100, null=True)
    Experience = models.CharField(max_length=100, null=True)
    TotalVacancy = models.CharField(max_length=100, null=True)
    JOBTYPE = [
        ('Full Time','Full Time'),
        ('Part Time','Part Time'),
        ('Contractual','Contractual'),
        ('Internship','Internship'),
        ('Freelance','Freelance'),
    ]
    JobType = models.CharField(choices=JOBTYPE, max_length=100, null=True)
    EXPERIENCELEVEL = [
        ('Begineer','Begineer'),
        ('Mid Level','Mid Level'),
        ('Experienced','Experienced'),
        ('TopLevel','TopLevel'),
    ]
    ExperienceLevel = models.CharField(choices=EXPERIENCELEVEL, max_length=100, null=True)
    Created_at = models.DateField(auto_now_add=True,null=True)
    Updated_at = models.DateField(auto_now=True,null=True)
    PostedBy = models.ForeignKey(IonicJobUserModel, on_delete =models.CASCADE, null=True)
    
    class Meta:
        ordering = ['Created_at']
        verbose_name = "Job Info"
        db_table = 'JobInfo_Table'
    
    def __str__(self):
        return self.JobTitle
    
class JobApplicantModel(models.Model):
    Applicant = models.ForeignKey(IonicJobUserModel,on_delete=models.CASCADE, related_name='applicantuser', null=True)
    Job = models.ForeignKey(JobInfoModel,on_delete=models.CASCADE, null=True)
    Skills= models.TextField(null=True)
    Status= models.CharField(max_length=100,default="Pending", null=True)
    
    class Meta:
        db_table = 'Applicant_Table'
    

