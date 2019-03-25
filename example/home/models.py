from django.db import models

# Create your models here.

class Home(models.Model):
	name = models.CharField(max_length=50)
	email = models.EmailField()
	contact = models.PositiveIntegerField(null=True, blank=True)
	address = models.TextField(null=True, blank=True)

	def __str__(self):
		return self.name
