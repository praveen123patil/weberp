from django import forms
from .models import Workorder,Production

class WorkorderForm(forms.ModelForm):

	class Meta:
		model = Workorder
		fields = '__all__'

class ProductionForm(forms.ModelForm):

	class Meta:
		model = Production
		exclude = ['sgst','dispatched_date','pack','dispatched']	