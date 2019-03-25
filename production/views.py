from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Workorder,Production
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

def dispatched(request, pk):
	dispatch = get_object_or_404(Production, pk=pk)
	dispatch.dispatch()
	return redirect('packorder')

def dispatch(self):
		self.dispatched = True
		self.dispatched_date = timezone.now()
		self.save()

def dispatch_bill(request, pk):
	dispatch_bill = get_object_or_404(Production, pk=pk)
	return render(request, 'production/print1.html', {'dispatch_bill' : dispatch_bill})

def dispatched_list(request):
	dispatched = Production.objects.filter(dispatched = True).order_by('dispatched_date')		
	return render(request, 'production/dispatched_list.html', {'dispatched': dispatched})

def packorder(request):
	dispatch = Production.objects.filter(pack = True ).filter(dispatched = False).order_by('production_date')
	return render(request, 'production/dispatch.html',{'dispatch':dispatch})

