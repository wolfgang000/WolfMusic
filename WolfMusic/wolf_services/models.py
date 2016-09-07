from django.db import models
from django.core.urlresolvers import reverse
from django.db.models.signals import post_save
from django.dispatch import receiver
import taglib

class Track(models.Model):
	TYPE_MP3 = "audio/mpeg"
	TYPE_OGG = "audio/ogg"
	FILE_TYPES = (
		(TYPE_MP3,"mp3"),
		(TYPE_OGG,"ogg"),
	)
	
	title = models.CharField(max_length=64,default="")
	album = models.CharField(max_length=64,default="")
	artist = models.CharField(max_length=64,default="")
	genre = models.CharField(max_length=64,default="")
	name = models.CharField(max_length=50,default="")
	type =  models.CharField(max_length=20, choices=FILE_TYPES)
	file = models.FileField(upload_to='music/tracks')
	def get_absolute_url(self):
		return reverse('tracks.detail', args=[str(self.id)])

@receiver(post_save, sender=Track, dispatch_uid="set_metadata")
def update_stock(sender, instance, **kwargs):
	print("postSave")
	song = taglib.File(instance.file.path)
	if len(song.tags['TITLE'])> 0:
		instance.title = song.tags['TITLE'][0]
	if len(song.tags['ALBUM']) > 0:
		instance.album = song.tags['ALBUM'][0]
	if len(song.tags['ARTIST']) > 0:
		instance.artist = song.tags['ARTIST'][0]
	if len(song.tags['GENRE']) > 0:
		instance.genre = song.tags['GENRE'][0]
		
	Track.objects.filter(pk=instance.pk).update(title=instance.title, album=instance.album, artist=instance.artist, genre=instance.genre)
		