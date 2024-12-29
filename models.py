from django.db import models
class permission(models.Model):
	name=models.CharField(max_length=50)
	food=models.CharField(max_length=50)
	price=models.FloatField(max_length=40)
	location=models.CharField(max_length=40)
