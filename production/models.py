from django.utils import timezone
from django.db import models
from master.models import Item,Customer

shift = [
	('1','Shift1'),
	('2','Shift2'),
	('3','Shift3'),
]

# Create your models here.
class Workorder(models.Model):
	Select_item = models.ForeignKey(Item, on_delete=models.CASCADE)
	Quantity = models.PositiveIntegerField(blank=True)
	Order_date = models.DateTimeField(default=timezone.now)
	Target_date = models.DateField()
	Select_customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

class Production(models.Model):
	production_date = models.DateTimeField(default=timezone.now)
	shift = models.CharField(max_length=1, choices=shift)
	item = models.ForeignKey(Item, on_delete=models.CASCADE)
	batch_number = models.DateField()
	total_production = models.PositiveIntegerField()
	

