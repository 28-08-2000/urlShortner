from django.db import models

# model to store link and uuid
class Url(models.Model):
	link = models.CharField(max_length=10000)
	uuid = models.CharField(max_length=10)