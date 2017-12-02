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


def results(request):
    context = {
    	'title': 'Search Results',
    }
    return render(request, 'polls/results.html', context)