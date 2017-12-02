from django.http import HttpResponse
from django.shortcuts import render

from .models import Question


def index(request):
    context = {
    	'title': 'Search Food',
    }
    return render(request, 'polls/index.html', context)