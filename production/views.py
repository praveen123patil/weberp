from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
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
	production = Production.objects.all()
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

def vieworder(request):
	return render(request, 'production/vieworder.html',)

def dispatch(request):
	return render(request, 'production/dispatch.html',)

