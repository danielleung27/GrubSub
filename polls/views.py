from django.http import HttpResponse
from django.shortcuts import render
from .forms import SearchForm

from .foother import FoodSearch

def index(request):
    return render(request, 'polls/index.html')

def result(request):
	context = {}

	if request.method == 'POST':
		query = request.POST.get('search_box')
		if query:
			data = FoodSearch()
			t = data.similar_entries(10, query)
			context['query'] = query
			context['food_list'] = t

	return render(request, 'polls/searchresult.html', context)

def directory(request):
	return render(request, 'polls/directory.html')