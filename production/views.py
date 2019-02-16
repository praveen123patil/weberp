from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here. 
def workorder(request):
	return render(request, 'production/workorder.html',)

def production(request):
	return render(request, 'production/production.html',)

def vieworder(request):
	return render(request, 'production/vieworder.html',)

def dispatch(request):
	return render(request, 'production/dispatch.html',)

