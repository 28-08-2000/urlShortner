from django.db import models
from account.models import Account

# Create your models here.

# create a class to store individuals info
class individual(models.Model):
	name = models.CharField(unique = True, max_length = 100)

	# gender is import to classify b/w father and mother
	gender = models.CharField(max_length=1, 
		choices=(('M', 'Male'), ('F', 'Female')),
		blank=False,
		default=None,
		)

	# # dob = models.DateField()

	# add the corresponding user of this tree
	user = models.CharField(max_length=30, blank=True, null=True)
	# user = models.ForeignKey('Account',		
	# 	models.SET_NULL,
	# 	blank=True,
	# 	null=True,
	# 	)

	mother = models.ForeignKey('self', 
		models.SET_NULL, 
		blank=True, 
		null=True,
		related_name='children_of_mother'
		)
	father = models.ForeignKey('self',
		models.SET_NULL,
		blank=True,
		null=True,
		related_name='child_of_father'
		)
	spouse = models.ForeignKey('self',
		models.SET_NULL,
		blank=True,
		null=True,
		related_name='Spouse'
		)

	def __str__(self):
		return self.name;

# let's create a relationship model
class relationship(models.Model):
	personA = models.CharField(max_length=100)
	personB = models.CharField(max_length=100)

	relation = models.CharField(max_length=20,
		choices=(('S', 'Spouse'), ('F', 'Father'), ('M', 'Mother')),
		blank=False,
		default=None,
		)

	def __str__(self):
		return self.personA+self.personB;
