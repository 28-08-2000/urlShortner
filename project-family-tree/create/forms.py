from django import forms
from django.forms import ModelForm
from .models import individual, relationship

# create individual form
class IndividualForm(ModelForm):
	class Meta:
		model = individual
		fields = ['name', 'gender']

		labels = {
			'name': 'Name',
			'gender': 'Gender',
		}

		widgets = {
			'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Name'}),
			'gender': forms.RadioSelect(attrs={'class': 'form-control', 'placeholder': 'Gender'}),
		}

# create a form to add relations ships
class RelationshipForm(ModelForm):
	class Meta:
		model = relationship 

		fields = ['personA', 'personB', 'relation']

		labels = {
			'personA': 'North',
			'personB': 'South',
			'relation': 'North is _ of South',
		}

		widgets = {
			'personA': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Member A'}),
			'personB': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Member B'}),
			'relation': forms.RadioSelect(attrs={'class': 'form-control', 'placeholder': 'Relationship'}),
		}
