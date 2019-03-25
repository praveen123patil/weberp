from django.shortcuts import render
from material_transaction.models import Purchase
import datetime

# Create your views here.
def report(request):
	return render(request,'report/report.html')

def purchase_report(request):
	error = False
	if 'from_date' and 'to_date' in request.GET:
		from_date = datetime.datetime.strptime(request.GET['from_date'], '%Y-%m-%d')
		to_date = datetime.datetime.strptime(request.GET['to_date'], '%Y-%m-%d')
		if not 'from_date':
			error = True
		elif not 'to_date':
			error = True
		else:
			purchase_report = Purchase.objects.filter(date_range=[from_date, to_date])
			return render(request, 'report/purchase_report.html', {'purchase_report':purchase_report})
	return render(request,'report/purchase_report.html',{'error':error})


