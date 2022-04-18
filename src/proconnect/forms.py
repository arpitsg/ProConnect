from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core import validators
from django.core.exceptions import ValidationError
GENDER=[
    ('M', 'Male'),
    ('F', 'Female'),
    ('O','Other'),
    ('S','Prefer not to say')
]
class NewUserForm(UserCreationForm):
	email = forms.EmailField(max_length=100,required = True,help_text='Enter Email Address',widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),)
	first_name = forms.CharField(max_length=100,required = True,help_text='Enter First Name',widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),)
	last_name = forms.CharField(max_length=100,required = True,help_text='Enter Last Name',widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),)
	gender=forms.ChoiceField( choices=GENDER)
	dob=forms.DateField(help_text='Enter date of birth',)
	username = forms.CharField(max_length=200,required = True,help_text='Enter Username',widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),)
	password1 = forms.CharField(help_text='Enter Password',required = True,widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),)
	password2 = forms.CharField(required = True,help_text='Enter Password Again',widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password Again'}),)
	def clean_username(self):
					username = self.cleaned_data['username'].lower()
					r = User.objects.filter(username=username)
					if r.count():
									raise  ValidationError("Username already exists")
					return username

	def clean_email(self):
					email = self.cleaned_data['email'].lower()
					r = User.objects.filter(email=email)
					if r.count():
									raise  ValidationError("Email already exists")
					return email

	def clean_password2(self):
					password1 = self.cleaned_data.get('password1')
					password2 = self.cleaned_data.get('password2')

					if password1 and password2 and password1 != password2:
									raise ValidationError("Password don't match")

					return password2
	def save(self, commit=True):
		print('=-----------saving')
		user = User.objects.create_user(
						self.cleaned_data['username'],
						self.cleaned_data['email'],
						self.cleaned_data['password2']
		)
		return user


	class Meta:
		model = User
		fields = ['email', 'first_name', 'last_name', 'gender', 'dob', 'username','password1', 'password2',]

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