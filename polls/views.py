from django.http import HttpResponse
from django.shortcuts import render

from .models import Question
from .forms import SearchForm

def search(request):
	form = SearchForm()
	context = {
		'title': 'Search Food',
		'form': form,
	}
	return render(request, 'polls/search_form.html', context)

def index(request):
    return render(request, 'polls/index.html')

def directory(request):
	return render(request, 'polls/directory.html')

def searchresult(request):
	return render(request, 'polls/searchresult.html')

def results(request):
    context = {
    	'title': 'Search Results',
    }
    return render(request, 'polls/results.html', context)
