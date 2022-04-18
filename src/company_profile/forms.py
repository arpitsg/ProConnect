from django import forms
from .models import Job,Company_profile,Application
class Job_form(forms.ModelForm):
    class Meta:
        model=Job
        fields=('title','description','location','experience_required','salary','skills_req','job_type','deadline')
        widgets = {
            'deadline': forms.DateInput(attrs={'type': 'date'}),
        }

class Update_profile(forms.ModelForm):
    class Meta:
        model=Company_profile
        fields=('company_name','location','about_us','employee_strength')
        # widgets = {
        #      'about_us': forms.TextField(),
        #  }
        
class Application_Update(forms.ModelForm):
    class Meta:
        model=Application
        fields=('status','comment')