from django import forms

from .models import SignUp


class ContactForm(forms.Form):
	full_name=forms.CharField(required=False)
	email=forms.EmailField()
	message=forms.CharField()

class SignUpForm(forms.ModelForm):
	class Meta:
		model=SignUp
		fields=['full_name','email']



	def clean_email(self):

		email= self.cleaned_data.get('email')
		if len(email)==0:
			raise forms.ValidationError("Enter valid email address")
		email_base,provider=email.split('@')
		domain,extension=provider.split('.')
		if 'edu' not in extension:
			raise forms.ValidationError("Oh Hello please provide a valid college email")
		return email