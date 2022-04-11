from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core import validators


class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user



#DataFlair #Custom_Validator
# def check_size(value):
#   if len(value) < 6:
#     raise forms.ValidationError("the Password is too short")

# #DataFlair #Form
# class SignUp(forms.Form):
#   first_name = forms.CharField(initial = 'First Name', )
#   last_name = forms.CharField(required = False)
#   email = forms.EmailField(help_text = 'write your email', required = False)
#   Address = forms.CharField(required = False, )
#   Technology = forms.CharField(initial = 'Django', disabled = True)
#   age = forms.IntegerField(required = False, )
#   password = forms.CharField(widget = forms.PasswordInput, validators = [check_size, ])
#   re_password = forms.CharField(widget = forms.PasswordInput, required = False)