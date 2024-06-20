from django import forms
from JobPortalApp.models import *

class JobForm(forms.ModelForm):
    class Meta:
        model = JobInfoModel
        fields = "__all__"
        exclude = ['PostedBy']
        
        widgets = {
            'Deadline':forms.DateInput(attrs={
              'type'  :'date'
            }),
            'Created_at':forms.DateInput(attrs={
                'type':'date'
            }),
            'Updated_at':forms.DateInput(attrs={
                'type':'date'
            })
        }
        
        labels = {
            "JobSummary":"Job Summary",
            "Experience":"Experience (in Year)",
            "TotalVacancy":"Total Vanancy",
            "JobResponsibilities":"Job Responsibilities",
            "RequiredSkills":"Required Skills",
            "AdditionalRequirement":"Additional Requirement",
            "JobBenefits":"Job Benefits",
            "JobType":"Job Type",
            "ExperienceLevel":"Experience Level",
            "JobCategories":"Job Categories",
        }