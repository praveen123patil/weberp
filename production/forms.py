from django import forms
from .models import Workorder,Production,Dispatch

class WorkorderForm(forms.ModelForm):

	class Meta:
		model = Workorder
		fields = '__all__'

class ProductionForm(forms.ModelForm):

	class Meta:
		model = Production
		fields = '__all__'		

class DispatchForm(forms.ModelForm):

	class Meta:
		model = Dispatch
		fields = '__all__'