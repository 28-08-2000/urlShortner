from django.shortcuts import render
from PyDictionary import PyDictionary
from bs4 import BeautifulSoup
import requests

# Create your views here.
def index(request):
	return render(request, 'index.html')

def word(request):
	search = request.GET.get('search')

	# get dictionary object
	dictionary = PyDictionary()

	# get meaning, synonyms, antonymsn
	meaning = dictionary.meaning(search)

	# NOT PRESENT NOW
	# synonyms = dictionary.synonym(search)
	# antonyms = dictionary.antonym(search)
	
	synonyms = MYsynonyms(search)

	# pass details through variable
	context = {
		'meaning': meaning['Noun'][0],
		'synonyms': synonyms,
		# 'antonyms': antonyms
	}

	# render new page
	return render(request, 'word.html', context)

# to get synonyms
def MYsynonyms(term):
    response = requests.get('https://www.thesaurus.com/browse/{}'.format(term))
    soup = BeautifulSoup(response.text, 'lxml')
    soup.find('section', {'class': 'css-17ofzyv e1ccqdb60'})
    return [span.text for span in soup.findAll('a', {'class': 'css-1kg1yv8 eh475bn0'})] # 'css-1gyuw4i eh475bn0' for less relevant synonyms
