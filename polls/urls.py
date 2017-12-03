from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^index$', views.index, name='index'),
    url(r'^directory$', views.directory, name='directory'),
	url(r'^searchresult$', views.searchresult, name='searchresult'),
	url(r'^$', views.search, name='search'),
    url(r'results/$', views.results, name='results'),
]