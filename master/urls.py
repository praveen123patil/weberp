from django.urls import path
from .import views

urlpatterns =[
	path('',views.master, name='master'),
	path('customer/', views.customer, name='customer'),
	path('customer/add-customer', views.newcustomer, name='newcustomer'),
	path('supplier/',views.supplier,name='supplier'),
	path('supplier/add-supplier', views.newsupplier, name='newsupplier'),
	path('item/',views.item, name='item'),
	path('item/add-item', views.newitem, name='newitem'),
	path('item/<int:pk>/edit', views.edititem, name='edititem'),
	path('item/<int:pk>/delete', views.deleteitem, name='deleteitem'),
	path('customer/<int:pk>/edit', views.editcustomer, name='editcustomer'),
	path('customer/<int:pk>/delete', views.deletecustomer, name='deletecustomer'),
	path('supplier/<int:pk>/edit', views.editsupplier, name='editsupplier'),
	path('supplier/<int:pk>/delete', views.deletesupplier, name='deletesupplier'),
	]