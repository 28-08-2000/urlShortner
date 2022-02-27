from django.shortcuts import render

# define 
def index(request):
	return render(request, 'index.html')