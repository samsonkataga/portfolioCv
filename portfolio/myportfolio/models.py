from django.db import models

# Create your models here.

class contact(models.Model):
	fullname = models.CharField(max_length=100)
	email = models.CharField(max_length=15)
	message	= models.CharField(max_length=100)
	def __str__(self):
		return self.fullname

