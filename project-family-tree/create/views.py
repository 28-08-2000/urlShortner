from django.shortcuts import render, redirect
from .models import individual, relationship
from .forms import IndividualForm, RelationshipForm
from .utils import *
from account.models import Account

# Create your views here.
def create(request):

	individuals = individual.objects.all()

	# if request is post, get details and save them
	if request.method == 'POST':
		form = IndividualForm(request.POST, request.FILES)

		if form.is_valid():
			new_individual = form.save(commit=False)

			new_individual.user = request.user.username
			new_individual.save()
			
		return redirect('/create')

	# create multiple trees
	trees = create_trees(request.user.username)
	print(trees)

	form = IndividualForm
	relationForm = RelationshipForm
	context = {
		# 'individuals': individuals,
		'form': form,
		'family': trees,
		'relationForm': relationForm,
	}

	return render(request, 'create.html', context)

def create_relation(request):

	# request.method == 'POST':
	form = RelationshipForm(request.POST, request.FILES)

	if form.is_valid():
		Relation = form.save(commit=False)
		Relation.save()

		# get the individuals
		individuals = individual.objects.all()
		
		north =  individuals.get(name=Relation.personA)
		south = individuals.get(name=Relation.personB)
		relation_ = Relation.relation

		print(north, south, relation_)

		if relation_ == 'S':
			north.spouse = south
			south.spouse = north
		elif relation_ == 'F':
			south.father = north 
		else:
			south.mother = north

		north.save()
		south.save()

	return redirect('/create')

def delete_ind(request, id):

	# get the individual name
	name = individual.objects.filter(id=id)[0].name

	# delete individual object
	individual.objects.filter(id=id).delete()

	# # delete relationship object
	relationship.objects.filter(personA=name).delete()
	relationship.objects.filter(personB=name).delete()

	return redirect('/create')

def create_parent(request, pk):

	# request.method == 'POST':
	form = IndividualForm(request.POST, request.FILES)

	if form.is_valid():
		new_individual = form.save(commit=False)
		new_individual.save()

		# add the parent
		individuals = individual.objects.all()
		curr = individuals.get(pk=pk)

		# check gender
		if new_individual.gender == 'M':
			curr.father = new_individual
		else:
			curr.mother = new_individual

		curr.save()

	return redirect('/create')
