from django.shortcuts import render, redirect
from .forms import HomeForm
from .models import Home

# Create your views here.

def home(request):
	if request.method == 'POST':
		form = HomeForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('home')
	else:
		form = HomeForm()
	return render(request,'home/home.html',{'form': form})
