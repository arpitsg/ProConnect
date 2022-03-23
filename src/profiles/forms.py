from attr import fields
from django import forms
from .models import Profile

class ProfileModilfy(forms.ModelForm):
    class Meta:
        model=Profile
        fields=('first_name', 'last_name','about_us','headline','picture')