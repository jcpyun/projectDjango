from django import forms
from .models import SignUp

#### new edit 15

class ContactForm(forms.Form):
	full_name = forms.CharField(required=False)
	email = forms.EmailField()
	message=forms.CharField()


class SignUpForm(forms.ModelForm):
	class Meta:
		model = SignUp
		fields = ['full_name','email']
		#exclude = ['full_name']
	def clean_email(self):
		email= self.cleaned_data.get('email')
		email_base, provider = email.split("@")
		if provider == "andrew.cmu.edu":
			return email
		else:
			domain,extension = provider.split('.')
			if not extension=="edu":
				raise forms.ValidationError("FUCK YOU USE EDU. BITCH")
		return email