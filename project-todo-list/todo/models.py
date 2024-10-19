from django.db import models

# my data classes
class Todo(models.Model):
	title = models.CharField(max_length = 1000)

	def __str__(self):
		return self.title