from django import forms

from .models import Codeline

class BasicForm(forms.ModelForm):
	class Meta:
		model = Codeline
		fields = ('__all__')


class LoginForm(forms.Form):
	username = forms.CharField(label="Username")
	password = forms.CharField(label="Password", widget=forms.PasswordInput)