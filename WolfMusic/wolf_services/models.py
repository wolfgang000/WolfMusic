from django.db import models
from django.core.urlresolvers import reverse

class Track(models.Model):
	TYPE_MP3 = "audio/mpeg"
	TYPE_OGG = "audio/ogg"
	FILE_TYPES = (
		(TYPE_MP3,"mp3"),
		(TYPE_OGG,"ogg"),
	)
	
	title = models.CharField(max_length=50)
	name = models.CharField(max_length=50)
	type =  models.CharField(max_length=20, choices=FILE_TYPES)
	file = models.FileField(upload_to='music/tracks')
	def get_absolute_url(self):
		return reverse('tracks.detail', args=[str(self.id)])