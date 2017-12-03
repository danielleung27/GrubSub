from django.conf.urls import url

from . import views

urlpatterns = [
	# url(r'^$', views.search, name='search'),
	url(r'^$', views.index, name='index'),
    url(r'^directory/$', views.directory, name='directory'),
	url(r'^results/$', views.searchresult, name='searchresult'),
    # url(r'results/$', views.results, name='results'),
]