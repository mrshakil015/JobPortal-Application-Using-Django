from django import forms
from JobPortalApp.models import *

class JobForm(forms.ModelForm):
    class Meta:
        model = JobInfoModel
        fields = "__all__"
        exclude = ['PostedBy']
        
        widgets = {
            'Deadline':forms.DateInput(attrs={
              'type'  :'date','class':'date-field'
            }),
            'Created_at':forms.DateInput(attrs={
                'type':'date'
            }),
            'Updated_at':forms.DateInput(attrs={
                'type':'date'
            })
        }
        
        labels = {
            "TotalVacancy":"Total Vanancy",
            "JobType":"Job Type",
            "ExperienceLevel":"Experience Level",
        }
