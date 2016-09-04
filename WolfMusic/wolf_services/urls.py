from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^track/$', views.TrackList.as_view(),name='track.list'),
]
