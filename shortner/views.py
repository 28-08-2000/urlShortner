from django.shortcuts import render, redirect
import uuid
from .models import Url
from django.http import HttpResponse

# define 
def index(request):
	return render(request, 'index.html')

# create shorted url
def create(request):
	if request.method == 'POST':

		# get the posted link
		link = request.POST['link']
		
		# create new url
		uid = str(uuid.uuid4())

		# save in url mode
		new_url = Url(link=link, uuid=uid)
		new_url.save()

		# return the response page
		return HttpResponse(uid)

def go(request, pk):
	# get the Url object
	url_details = Url.objects.get(uuid=pk)

	# redidrect to original website
	return redirect('https://' + url_details.link)
