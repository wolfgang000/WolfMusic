from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework import authentication, permissions
from rest_framework import status
from django.urls import reverse
from django.http import Http404
from . import serializers
from . import models


class RootService(APIView):
	def get(self, request, format=None):
		data={}
		data['track_url'] = request.build_absolute_uri(reverse('track.list'))
		data['album_url'] = request.build_absolute_uri(reverse('album.list'))
		return Response(data)

class TrackDetail(APIView):
	
	def get_object(self, pk):
		try:
			return models.Track.objects.get(pk=pk)
		except models.Track.DoesNotExist:
			raise Http404

	def get(self, request, pk, format=None):
		obj = self.get_object(pk)
		serializer = serializers.Track(obj,context={'request':request})
		return Response(serializer.data)

	def delete(self, request, pk, format=None):
		obj = self.get_object(pk)
		del obj
		return Response(status=status.HTTP_200_OK)

class AlbumDetail(APIView):
	
	def get_object(self, pk):
		try:
			return models.Album.objects.get(pk=pk)
		except models.Album.DoesNotExist:
			raise Http404

	def get(self, request, pk, format=None):
		obj = self.get_object(pk)
		serializer = serializers.Album(obj,context={'request':request})
		return Response(serializer.data)

	def delete(self, request, pk, format=None):
		obj = self.get_object(pk)
		del obj
		return Response(status=status.HTTP_200_OK)

class TrackList(APIView):
	parser_classes = (MultiPartParser, FormParser,)
	def get(self, request, format=None):
		tracks = models.Track.objects.all()
		serializer = serializers.Track(tracks, many=True,context={'request':request})
		return Response(serializer.data)
		
	def post(self, request, format=None):
		files = request.FILES.getlist('file')
		tracks = []
		for file in files:
			track = models.Track()
			track.file = file
			track.name = file.name
			track.save()
			track.updateMetadataSave()
			tracks.append(track)
			
		serializer = serializers.Track(tracks,many=True,)
		return Response(serializer.data,status=status.HTTP_201_CREATED)

class AlbumList(APIView):
	def get(self, request, format=None):
		objs = models.Album.objects.all()
		serializer = serializers.Album(objs, many=True,context={'request':request})
		return Response(serializer.data)
		