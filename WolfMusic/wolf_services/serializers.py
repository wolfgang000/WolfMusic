from rest_framework import serializers
from . import models

class Track(serializers.ModelSerializer):
	class Meta:
		model = models.Track
		fields = ('title','file',)
		read_only_fields = ('title', 'file',)