from django.db import models
from datetime import date

# Create your models here.
class Table(models.Model):
	name = models.CharField(max_length = 200)
	location = models.CharField(max_length=200)
	product = models.CharField(max_length=200)
	mobile = models.CharField(max_length=200)
	amount = models.CharField(max_length=200)
	created = models.DateTimeField(auto_now_add=True,default=date.now())

	def __str__(self):
		return self.name

