from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^root/$', views.RootService.as_view(),name='root'),
	url(r'^tracks/$', views.TrackList.as_view(),name='track.list'),
	url(r'^albums/$', views.AlbumList.as_view(),name='album.list'),
	url(r'^tracks/(?P<pk>\d+)/$', views.TrackDetail.as_view(),name='track.detail'),
	url(r'^albums/(?P<pk>\d+)/$', views.AlbumDetail.as_view(),name='album.detail'),
]
