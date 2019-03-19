from django.utils import timezone
from django.db import models
from master.models import Supplier
# Create your models here.
class Rawitem(models.Model):
	itemcode = models.CharField(max_length=50)
	item_name = models.CharField(max_length=10)
	rate = models.PositiveIntegerField(blank=True)
	description = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.item_name

class Purchase(models.Model):
	rawitem=models.ForeignKey(Rawitem, on_delete=models.CASCADE)
	quantity=models.PositiveIntegerField(blank=True)
	date=models.DateTimeField(default=timezone.now)
	supplier=models.ForeignKey(Supplier, on_delete=models.CASCADE)
	total=models.PositiveIntegerField(editable=False)
	receives=models.BooleanField(default=False)
	counts=models.PositiveIntegerField(null=True, blank=True)
	sgst=models.FloatField(null=True, blank=True, editable=False)
	grand_total=models.PositiveIntegerField(editable=False)


	def __str__(self):
		return self.rawitem

	def save(self,*args,**kwargs):
		self.total = self.rawitem.rate*self.quantity
		self.sgst = (self.total/100)*9	
		self.grand_total = self.sgst+self.total
		self.counts = 0
		self.counts = self.counts+self.quantity
		super(Purchase, self).save(*args,**kwargs)

	def received(self):
		self.receives = True
		self.save()

	def count(self, *args, **kwargs):
		self.counts = self.counts + self.quantity
		super(Purchase, self).save(*args, **kwargs)