from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Workorder,Production, Dispatch
from .forms import WorkorderForm,ProductionForm
# Create your views here.
def workorder(request):
	workorder = Workorder.objects.all()
	return render(request, 'production/workorder.html',{'workorder': workorder})

def new_workorder(request):
	if request.method == "POST":
		form = WorkorderForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('workorder')
	else: 
		form = WorkorderForm()
	return render(request, 'production/new-workorder.html', {'form':form})

def production(request):
	production = Production.objects.filter(pack = False).order_by('production_date')
	return render(request, 'production/production.html',{'production': production})

def new_production(request):
	if request.method == "POST":
		form = ProductionForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('production')
	else: 
		form = ProductionForm()
	return render(request, 'production/new-production.html', {'form':form})

def item_packed(request, pk):
	packed = get_object_or_404(Production, pk=pk)
	packed.packed()
	return redirect('production')

def packed(self):
		self.pack = True
		self.save()

def dispatch(request, pk):
	dispatch = get_object_or_404(Production, pk=pk)
	return render(request, 'production/dispatch-details.html', {'dispatch': dispatch})

def dispatch_entry(request):
	if request.method == 'POST':
		if request.POST.get('item') and request.POST.get('Quantity') and request.POST.get('price') and request.POST.get('total') and request.POST.get('Select_customer') and request.POST.get('dispatch_date'):
			post=Dispatch()
			post.item = request.POST('item')
			post.Quantity = request.POST('Quantity')
			post.Price = request.POST('Price')
			post.total = request.POST('total')
			post.Select_customer = request.POST('Select_customer')
			post.dispatch_date = request.POST('dispatch_date')
			post.save()

			return render(request,'production/dispatch-details.html')
	else:
		return render(request,'production/dispatch-details.html')


def packorder(request):
	dispatch = Production.objects.filter(pack = True).order_by('production_date')
	return render(request, 'production/dispatch.html',{'dispatch':dispatch})

