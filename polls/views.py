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
			food_list = []
			t = data.similar_entries(10, query)
			for i in range(len(t)):
				first_word = t[i]
				rest_word = ""
				if(len(t[i].split(", ", 1)) > 1):
					first_word, rest_word = t[i].split(", ", 1)
				food_list.append((first_word, rest_word))
			context['query'] = query
			context['food_list'] = food_list

	return render(request, 'polls/searchresult.html', context)

def directory(request):
	context = {}

	data = FoodSearch()
	ds = data.return_dataset()
	context['data_set'] = ds
	return render(request, 'polls/directory.html', context)