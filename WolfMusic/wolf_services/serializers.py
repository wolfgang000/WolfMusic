from rest_framework import serializers
from . import models
from django.contrib.sites.shortcuts import get_current_site

class BaseClass():
	def get_full_url(self, obj):
		request = self.context.get('request', None)
		if request is not None:
			current_site = get_current_site(request)
			return 'http://%s%s' % (current_site, obj.get_absolute_url()) 
		else:
			return obj.get_absolute_url()


class Track(serializers.ModelSerializer,BaseClass):
	url = serializers.SerializerMethodField('get_full_url', read_only=True)
	class Meta:
		model = models.Track
		fields = ('url','id','title','file',)
		read_only_fields = ('url','id','title', 'file',)