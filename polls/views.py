from django.http import HttpResponse
from django.shortcuts import render
from .forms import SearchForm

def index(request):
    return render(request, 'polls/results.html')

def searchresult(request):
	return render(request, 'polls/searchresult.html')

def directory(request):
	return render(request, 'polls/directory.html')

