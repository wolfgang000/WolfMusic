from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework import authentication, permissions
from rest_framework import status
from . import serializers
from . import models


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

class TrackList(APIView):
	parser_classes = (MultiPartParser, FormParser,)
	def get(self, request, format=None):
		tracks = models.Track.objects.all()
		serializer = serializers.Track(tracks, many=True,)
		return Response(serializer.data)
		
	def post(self, request, format=None):
		file_obj = request.FILES['file']
		title = request.data['title']
		track = models.Track()
		track.file = file_obj;
		track.title = title 
		track.save()
		serializer = serializers.Track(track)
		return Response(serializer.data, status=status.HTTP_201_CREATED)