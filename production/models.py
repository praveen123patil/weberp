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
	total=models.PositiveIntegerField(editable=False)
	Select_customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

	def save(self,*args,**kwargs):
		self.total = self.Select_item.price*self.Quantity
		super(Workorder, self).save(*args,**kwargs)

class Production(models.Model):
	Workorder_id = models.ForeignKey(Workorder, on_delete=models.CASCADE)
	production_date = models.DateTimeField(default=timezone.now)
	shift = models.CharField(max_length=1, choices=shift)
	item = models.ForeignKey(Item, on_delete=models.CASCADE)
	batch_number = models.PositiveIntegerField()
	total_production = models.PositiveIntegerField()
	pack=models.BooleanField(default=False)
	dispatched=models.BooleanField(default=False)
	dispatched_date = models.DateField(null=True)
	sgst=models.FloatField(blank=True)
	grand_total=models.PositiveIntegerField(editable=False)


	def packed(self):
		self.pack = True
		self.save()

	def save(self,*args,**kwargs):
		self.sgst = (self.Workorder_id.total/100)*9	
		self.grand_total = self.sgst+self.Workorder_id.total
		super(Production, self).save(*args,**kwargs)
	
	def dispatch(self):
		self.dispatched = True
		self.dispatched_date = timezone.now()
		self.save()
	


