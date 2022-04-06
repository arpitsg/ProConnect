from attr import fields
from django import forms
from .models import Profile,Skills

class ProfileModilfy(forms.ModelForm):
    class Meta:
        model=Profile
        fields=('first_name', 'last_name','about_us','headline','picture')
class SkillModilfy(forms.ModelForm):
    class Meta:
        model=Skills
        fields=('title', 'proficiency')

