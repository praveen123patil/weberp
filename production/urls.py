from django.urls import path
from .import views

urlpatterns =[
	path('workorder/', views.workorder, name='workorder'),
	path('workorder/new-workorder/', views.new_workorder , name='new_workorder'),
	path('production/', views.production, name='production'),
	path('production/new-production/', views.new_production , name='new_production'),
	path('vieworder/', views.vieworder,name='vieworder'),
	path('dispatch/', views.dispatch, name='dispatch'),
	]