from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^root/$', views.RootService.as_view(),name='root'),
	url(r'^tracks/$', views.TrackList.as_view(),name='tracks.list'),
	url(r'^tracks/(?P<pk>\d+)/$', views.TrackDetail.as_view(),name='tracks.detail'),
]
