from django.http import HttpResponse
from django.shortcuts import render

from .models import Question


def index(request):
    return render(request, 'polls/index.html')

def directory(request):
	return render(request, 'polls/directory.html')

def searchresult(request):
	return render(request, 'polls/searchresult.html')