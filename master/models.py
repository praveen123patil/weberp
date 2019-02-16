from django.db import models
from django.utils import timezone

# Create your models here.

class Customer(models.Model):
	name = models.CharField(max_length=50)
	contact = models.PositiveIntegerField(max_length=10)
	email_id = models.EmailField(max_length=254, blank=True)
	address = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.name

class Supplier(models.Model):
	name = models.CharField(max_length=50)
	contact = models.PositiveIntegerField(max_length=10)
	email_id = models.EmailField(max_length=254, blank=True)
	address = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.name

class Item(models.Model):
	item_code = models.CharField(max_length=10)
	item_name = models.CharField(max_length=50)
	price = models.PositiveIntegerField()
	description = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.item_name



