from django.db import models
from django.core.urlresolvers import reverse

class Track(models.Model):
	title = models.CharField(max_length=50)
	file = models.FileField(upload_to='music/tracks')
	def get_absolute_url(self):
		return reverse('tracks.detail', args=[str(self.id)])