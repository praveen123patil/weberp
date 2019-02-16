from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Customer, Supplier, Item
from .forms import CustomerForm, SupplierForm,  ItemForm
from django.shortcuts import get_object_or_404


# Create your views here.
@login_required
def master(request):
	return render(request, 'master/master.html',)

@login_required
def customer(request):
	cust = Customer.objects.all()
	return render(request, 'master/customer.html', {'cust': cust})

@login_required
def newcustomer(request):
	if request.method == "POST":
		form = CustomerForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('customer')
	else:
		form = CustomerForm()
	return render(request, 'master/newcustomer.html', {'form': form})

@login_required
def supplier(request):
	supp = Supplier.objects.all()
	return render(request, 'master/supplier.html', {'supp': supp})


@login_required
def newsupplier(request):
	if request.method == "POST":
		form = SupplierForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('supplier')
	else:
		form = SupplierForm()
	return render(request, 'master/newsupplier.html', {'form': form})


@login_required
def newitem(request):
	if request.method == "POST":
		form = ItemForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('item')
	else:
		form = ItemForm()
	return render(request, 'master/newitem.html', {'form': form})


@login_required
def item(request):
	item= Item.objects.all()
	return render(request, 'master/item.html', {'item': item})

@login_required
def edititem(request, pk):
	item = get_object_or_404(Item, pk=pk)
	if request.method == "POST":
		form = ItemForm(request.POST, instance=item)
		if form.is_valid():
			form.save()
			return redirect('item')
	else:
		form = ItemForm(instance=item)
	return render(request, 'master/newitem.html', {'form': form})

@login_required
def deleteitem(request, pk):
	item = get_object_or_404(Item, pk=pk)
	item.delete()
	return redirect('item')

@login_required
def editcustomer(request,pk):
	customer = get_object_or_404(Customer, pk=pk)
	if request.method == "POST":
		form = CustomerForm(request.POST, instance=customer)
		if form.is_valid():
			form.save()
			return redirect('customer')
	else:
		form = CustomerForm(instance=customer)
	return render(request, 'master/newcustomer.html', {'form': form})	

@login_required
def deletecustomer(request, pk):
	customer = get_object_or_404(Customer, pk=pk)
	customer.delete()
	return redirect('customer')

@login_required
def editsupplier(request,pk):
	supplier = get_object_or_404(Supplier, pk=pk)
	if request.method == "POST":
		form = SupplierForm(request.POST, instance=supplier)
		if form.is_valid():
			form.save()
			return redirect('supplier')
	else:
		form = SupplierForm(instance=supplier)
	return render(request, 'master/newsupplier.html', {'form': form})	

@login_required
def deletesupplier(request, pk):
	customer = get_object_or_404(Supplier, pk=pk)
	customer.delete()
	return redirect('supplier')
