from rest_framework import serializers
from . import models
from django.contrib.sites.shortcuts import get_current_site

class BaseClass():
	def get_full_url(self, obj):
		request = self.context.get('request', None)
		if request is not None:
			return request.build_absolute_uri(obj.get_absolute_url()) 
		else:
			return obj.get_absolute_url()


class Track(serializers.ModelSerializer,BaseClass):
	url = serializers.SerializerMethodField('get_full_url', read_only=True)
	album = serializers.SerializerMethodField('_get_album', read_only=True)
	def _get_album(self, obj):
		if obj.album != None:
			request = self.context.get('request', None)
			if request is not None:
				return AlbumSummary(obj.album,context={'request':request}).data
			else:
				return AlbumSummary(album).data
		else :
			return None
	
	class Meta:
		model = models.Track
		fields = ('url','id','file','name','type','title','album','artist','genre','artwork',)
		read_only_fields = ('url','id','title','file','name','type','album','artist','genre','artwork',)

class TrackSummary(serializers.ModelSerializer,BaseClass):
	url = serializers.SerializerMethodField('get_full_url', read_only=True)
	class Meta:
		model = models.Track
		fields = ('id','title','url',)
		read_only_fields = ('url','id','title',)

class Album(serializers.ModelSerializer,BaseClass):
	url = serializers.SerializerMethodField('get_full_url', read_only=True)
	tracks = serializers.SerializerMethodField('_get_tracks', read_only=True)
	
	def _get_tracks(self, obj):
		tracks = models.Track.objects.filter(album = obj)
		request = self.context.get('request', None)
		if request is not None:
			return TrackSummary(tracks, many=True,context={'request':request}).data
		else:
			return TrackSummary(tracks, many=True).data
	
	class Meta:
		model = models.Track
		fields = ('url','id','name','tracks')
		read_only_fields = ('url','id','name','tracks')

class AlbumSummary(serializers.ModelSerializer,BaseClass):
	url = serializers.SerializerMethodField('get_full_url', read_only=True)
	class Meta:
		model = models.Track
		fields = ('url','id','name',)
		read_only_fields = ('url','id','name',)