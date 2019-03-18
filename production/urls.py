from django.urls import path
from .import views

urlpatterns =[
	path('workorder/', views.workorder, name='workorder'),
	path('workorder/new-workorder/', views.new_workorder , name='new_workorder'),
	path('production/', views.production, name='production'),
	path('production/new-production/', views.new_production , name='new_production'),
	path('packorder/', views.packorder,name='packorder'),
	path('dispatched/<int:pk>/', views.dispatched, name='dispatched'),
	path('dispatch_bill/<int:pk>', views.dispatch_bill, name='dispatch_bill'),
	path('item_packed/<int:pk>', views.item_packed, name='item_packed'),
	path('dispatched_list/', views.dispatched_list, name='dispatched_list'),
	]