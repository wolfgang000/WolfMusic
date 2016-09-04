from django.db import models

class Track(models.Model):
	title = models.CharField(max_length=50)
	file = models.FileField(upload_to='music/tracks')