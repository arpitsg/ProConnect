from attr import fields
from django import forms
from .models import Profile,Skills,Languages,Experience,Education , Projects
from django.forms.widgets import DateInput # need to import
class ProfileModilfy(forms.ModelForm):
    class Meta:
        model=Profile
        fields=('first_name', 'last_name','about_us','headline','picture')

        
class SkillModilfy(forms.ModelForm):
    class Meta:
        model=Skills
        fields=('title', 'proficiency')


class LangModilfy(forms.ModelForm):
    class Meta:
        model=Languages
        fields=('language_name', 'proficiency')


class ExperienceModify(forms.ModelForm):
    class Meta:
        model=Experience
        fields=('title','employement_type','company_name','description','start_date','end_date','description','is_current')
        widgets = {
            'start_date': DateInput(attrs={'type': 'date'}),
            'end_date':DateInput(attrs={'type': 'date'})
        }
class EducationModify(forms.ModelForm):
    class Meta:
        model=Education
        fields=('school','degree','field','start_date','end_date_expected','grade','description')
        widgets = {
            'start_date': DateInput(attrs={'type': 'date'}),
            'end_date_expected':DateInput(attrs={'type': 'date'})
        }
class ProjectModify(forms.ModelForm):
    class Meta:
        model=Projects
        fields=('title','start_date','end_date','mentor','description','status')
        widgets = {
            'start_date': DateInput(attrs={'type': 'date'}),
            'end_date':DateInput(attrs={'type': 'date'})
        }
        
