from django import forms
from .models import Customer , Supplier, Item


class CustomerForm(forms.ModelForm):

	class Meta:
		model = Customer
		fields = ('name','contact','email_id','address',)


class SupplierForm(forms.ModelForm):

	class Meta:
		model = Supplier
		fields = ('name','contact','email_id','address',)

class ItemForm(forms.ModelForm):

	class Meta:
		model = Item
		fields = ('item_code','item_name','price','description',)

