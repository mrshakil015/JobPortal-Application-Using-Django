from django.db import models
from django.contrib.auth.models import AbstractUser

class IonicJobUser(AbstractUser):
    USERTYPE = [
        ('Employer','Employer'),
        ('Seeker','Seeker'),
    ]
    UserType = models.CharField(choices=USERTYPE,max_length=50, null=True)
    
    class Meta:
        db_table = 'IonicJob_User_Table'
    

