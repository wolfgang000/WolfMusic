import os.path
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework import authentication, permissions
from rest_framework import status
from django.urls import reverse
import taglib
from . import serializers
from . import models


class RootService(APIView):
	def get(self, request, format=None):
		data={}
		data['tracks_url'] = request.build_absolute_uri(reverse('tracks.list'))
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

class TrackList(APIView):
	parser_classes = (MultiPartParser, FormParser,)
	def get(self, request, format=None):
		tracks = models.Track.objects.all()
		serializer = serializers.Track(tracks, many=True,context={'request':request})
		return Response(serializer.data)
		
	def post(self, request, format=None):
		file = request.FILES['file']
		track = models.Track()
		track.file = file
		track.name = file.name
		
		fileName, fileExtension = os.path.splitext(track.name)
		if(fileExtension == '.mp3'):
			track.type = models.Track.TYPE_MP3
		elif(fileExtension == '.ogg'):
			track.type = models.Track.TYPE_OGG
		
		track.save()
		serializer = serializers.Track(track)
		return Response(serializer.data, status=status.HTTP_201_CREATED)