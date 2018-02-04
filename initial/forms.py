from django import forms

from .models import Codeline

class BasicForm(forms.ModelForm):
	class Meta:
		model = Codeline
		fields = ('__all__')