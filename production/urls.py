from django.urls import path
from .import views

urlpatterns =[
	path('workorder/', views.workorder, name='workorder'),
	path('workorder/new-workorder/', views.new_workorder , name='new_workorder'),
	path('production/', views.production, name='production'),
	path('production/new-production/', views.new_production , name='new_production'),
	path('packorder/', views.packorder,name='packorder'),
	path('dispatch/<int:pk>/', views.dispatch, name='dispatch'),
	path('item_packed/<int:pk>', views.item_packed, name='item_packed'),
	]