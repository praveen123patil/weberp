from django import forms
from .models import Rawitem,Purchase

class RawitemForm(forms.ModelForm):

	class Meta:
		model = Rawitem
		fields = '__all__'

class PurchaseForm(forms.ModelForm):

	class Meta:
		model = Purchase
		exclude = ['receives','counts']