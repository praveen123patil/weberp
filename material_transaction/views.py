from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Rawitem, Purchase
from .forms import RawitemForm,PurchaseForm
from django.shortcuts import get_object_or_404
# Create your views here.
def raw_item_master(request):
	rawitem = Rawitem.objects.all()
	return render(request, 'material/raw-item-master.html',{'rawitem': rawitem})

def newrawitem(request):
	if request.method == "POST":
		form = RawitemForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('raw_item_master')
	else:
		form = RawitemForm()
	return render(request, 'material/newrawitem.html',{'form': form})

def editrawitem(request, pk):
	rawitem = get_object_or_404(Rawitem, pk=pk)
	if request.method == "POST":
		form = RawitemForm(request.POST, instance=rawitem)
		if form.is_valid():
			form.save()
			return redirect('raw_item_master')
	else:
		form = RawitemForm(instance=rawitem)
	return render(request, 'material/newrawitem.html', {'form': form})

def deleterawitem(request, pk):
	rawitem = get_object_or_404(Rawitem, pk=pk)
	rawitem.delete()
	return redirect('raw_item_master')

def purchase(request):
	if request.method == "POST":
		form = PurchaseForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('purchase_order')
	else:
		form = PurchaseForm()
	return render(request, 'material/purchase.html', {'form': form})

def purchase_bill(request, pk):
	purchase_bill = get_object_or_404(Purchase, pk=pk)
	return render(request,'material/print.html', {'purchase_bill' : purchase_bill})

def purchase_order_list(request):
	orderlist=Purchase.objects.filter(receives = False).order_by('date')
	return render(request,'material/purchase_order_list.html',{'orderlist':orderlist})

def material_received(request, pk):
	material = get_object_or_404(Purchase, pk=pk)
	material.received()
	return redirect('purchase_order')


def received(self):
	self.receives = True
	self.save()
	
def material_received_list(request):
	materials = Purchase.objects.filter(receives = True).order_by('date')
	return render(request, 'material/recieved.html',{'materials':materials})

def stock(request):
	return render(request, 'material/stock.html',)