from django.shortcuts import render, redirect
from .models import Todo

# Create your views here.
def index(request):

	todo = Todo.objects.all()

	# if a form is submitted
	if request.method == 'POST':
		
		# create new Todo objects
		new_todo = Todo(
				title = request.POST['title']
			)
		new_todo.save()

		return redirect('/')

	return render(request, 'index.html', {'todos': todo})  # render this page

def delete(request, pk):

	# get specific task
	todo = Todo.objects.get(id=pk)

	# delete the clicked task
	todo.delete()

	return redirect('/')
