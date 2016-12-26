from rest_framework import serializers
from django.core.urlresolvers import reverse

class TrackSerializer(serializers.Serializer):
	id = serializers.IntegerField()
	title = serializers.CharField(max_length=256)
	track_number = serializers.IntegerField()
	url = serializers.SerializerMethodField()
	
	def get_url(self, obj):
		return reverse('track.detail', args=[str(obj.id)])