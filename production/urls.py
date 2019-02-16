from django.urls import path
from .import views

urlpatterns =[
	path('workorder/', views.workorder, name='workorder'),
	path('production/', views.production, name='production'),
	path('vieworder/', views.vieworder,name='vieworder'),
	path('dispatch/', views.dispatch, name='dispatch'),
	]