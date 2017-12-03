from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
    url(r'^results/$', views.searchresult, name='searchresult'),
    url(r'^directory/$', views.directory, name='directory'),
]