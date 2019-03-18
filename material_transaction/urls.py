from django.urls import path
from .import views

urlpatterns =[
	path('raw-item-master/',views.raw_item_master, name='raw_item_master'),
	path('raw_item/add-item/', views.newrawitem , name='newrawitem'),
	path('purchase-order/',views.purchase,name='purchase'),
	path('material_received_list/',views.material_received_list,name='material_received_list'),
	path('purchase_bill/<int:pk>', views.purchase_bill, name='purchase_bill'),
	path('stock/',views.stock,name='stock'),
	path('raw_item/<int:pk>/edit', views.editrawitem, name='editrawitem'),
	path('raw_item/<int:pk>/delete', views.deleterawitem, name='deleterawitem'),
	path('purchase-order/list', views.purchase_order_list, name='purchase_order'),
	path('material_received/<int:pk>', views.material_received, name='material_received'),

]	