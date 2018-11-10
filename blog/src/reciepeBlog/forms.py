from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class ContactForm(forms.Form):
	fullname = forms.CharField(
		widget=forms.TextInput(
				attrs={"class":"form-control","placeholder":"Your full name","id":"form_full_name"
				}
			)
		)
	email 	 = forms.EmailField(
		widget=forms.EmailInput(
				attrs={"class":"form-control","placeholder":"Your email","id":"your_email"
				}
			)
		)
	content  = forms.CharField(
		widget=forms.Textarea(
				attrs={"class":"form-control","placeholder":"Your message"
				}
			)
		)

	# This is for email validation checking.
	# def clean_email(self):
	# 	email = self.cleaned_data.get("email")
	# 	if not "gmail.com" in email:
	# 		raise forms.ValidationError("Email has to be gmail.com")
	# 	return email
	

	# """docstring for ClassName"""
	# def __init__(self, arg):
	# 	super(ClassName, self).__init__()
	# 	self.arg = arg

class LoginForm(forms.Form):
	
	username = forms.CharField(label='User Name',
		widget=forms.TextInput(
				attrs={"class":"form-control","placeholder":"Username","id":"form_username"
				}
			)
		)
	password = forms.CharField(
		widget=forms.PasswordInput(
				attrs={"class":"form-control","placeholder":"Your password","id":"form_password"
				}
			)
		)

class RegisterForm(forms.Form):
	
	username = forms.CharField(label='User Name',
		widget=forms.TextInput(
				attrs={"class":"form-control","placeholder":"User name","id":"form_username"
				}
			)
		)
	email 	 = forms.EmailField(
		widget=forms.EmailInput(
				attrs={"class":"form-control","placeholder":"Your email","id":"your_email"
				}
			)
		)
	password = forms.CharField(
		widget=forms.PasswordInput(
				attrs={"class":"form-control","placeholder":"Your password","id":"form_password"
				}
			)
		)
	password2 = forms.CharField(label='Confirm password',
		widget=forms.PasswordInput(
				attrs={"class":"form-control","placeholder":"Your password","id":"form_password"
				}
			)
		)

	def clean_username(self):
		username = self.cleaned_data.get('username')
		query_set = User.objects.filter(username=username)
		if query_set.exists():
			raise forms.ValidationError('User name has already taken!')
		return username	
		
	def clean_email(self):
		email = self.cleaned_data.get('email')
		query_set = User.objects.filter(email=email)
		if query_set.exists():
			raise forms.ValidationError('User email has already taken!')
		return email	

	def clean(self):
		data = self.cleaned_data
		password = self.cleaned_data.get('password')
		password2 = self.cleaned_data.get('password2')
		if password2 != password:
			raise forms.ValidationError('Passwords mismatch.')
		return data