from django.urls import path
from .import views

urlpatterns = [
	path('',views.report, name='report'),
	path('purchase_report',views.purchase_report, name='purchase_report'),

]