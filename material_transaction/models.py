from django.utils import timezone
from django.db import models
from master.models import Supplier
# Create your models here.
class Rawitem(models.Model):
	itemcode = models.CharField(max_length=50)
	item_name = models.CharField(max_length=10)
	rate = models.PositiveIntegerField(max_length=254, blank=True)
	description = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.item_name

class Purchase(models.Model):
	rawitem=models.ForeignKey(Rawitem, on_delete=models.CASCADE)
	quantity=models.PositiveIntegerField(max_length=254, blank=True)
	date=models.DateTimeField(default=timezone.now)
	supplier=models.ForeignKey(Supplier, on_delete=models.CASCADE)
	total=models.PositiveIntegerField(editable=False)

	def __str__(self):
		return self.rawitem


	def save(self,*args,**kwargs):
		self.total = self.rawitem.rate*self.quantity
		super(Purchase, self).save(*args,**kwargs)
