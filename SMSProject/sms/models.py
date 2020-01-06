from django.db import models

# Create your models here.
class Table(models.Model):
	name = models.CharField(max_length = 200)
	location = models.CharField(max_length=200)
	product = models.CharField(max_length=200)
	mobile = models.CharField(max_length=200)
	amount = models.CharField(max_length=200)

	def __str__(self):
		return self.name

