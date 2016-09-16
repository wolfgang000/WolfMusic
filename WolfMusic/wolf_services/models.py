import os.path
from django.db import models
from django.core.urlresolvers import reverse
from django.core.files.base import ContentFile
from django.dispatch import receiver
import taglib
from mutagen import File

class Album(models.Model):
	name = models.CharField(max_length=64,default="")
	
	def get_absolute_url(self):
		return reverse('album.detail', args=[str(self.id)])

class Artist(models.Model):
	name = models.CharField(max_length=64,default="")
	
class Track(models.Model):
	TYPE_MP3 = "audio/mpeg"
	TYPE_OGG = "audio/ogg"
	FILE_TYPES = (
		(TYPE_MP3,"mp3"),
		(TYPE_OGG,"ogg"),
	)
	artwork = models.ImageField(upload_to='music/tracks')
	title = models.CharField(max_length=64,default="")
	album = models.ForeignKey(Album, on_delete=models.CASCADE, null = True)
	artist = models.CharField(max_length=64,default="")
	genre = models.CharField(max_length=64,default="")
	name = models.CharField(max_length=50,default="")
	type =  models.CharField(max_length=20, choices=FILE_TYPES)
	file = models.FileField(upload_to='music/tracks')
	
	def get_absolute_url(self):
		return reverse('track.detail', args=[str(self.id)])
	
	
	def updateMetadataSave(self):
		self.updateMetadata()
		self.save()
	
	def setFieldFromTags(self,tags,tag_title,field_name):
		if tags.get(tag_title) != None:
			field = ''
			for tag_title in tags.get(tag_title):
				field = getattr(self, field_name)
				field = ''
				field += tag_title + ' '
			setattr(self, field_name, field)

	def updateMetadata(self):
		song = taglib.File(self.file.path)		
		self.setFieldFromTags(song.tags,'TITLE','title')
		if song.tags.get('ALBUM') != None:
			for album_name in song.tags.get('ALBUM'):
				try:
					album = Album.objects.get(name=album_name)
					self.album = album
				except Album.DoesNotExist:
					new_album = Album(name=album_name)
					new_album.save()
					self.album = new_album

		self.setFieldFromTags(song.tags,'ARTIST','artist')
		self.setFieldFromTags(song.tags,'GENRE','genre')
		file = File(self.file.path)
		if file.tags != None:
			for tag in file.tags:
				if tag.startswith("APIC"):
					artwork = file.tags[tag].data
					self.artwork.save('art.jpg',ContentFile(artwork))
					break

		fileName, fileExtension = os.path.splitext(self.file.name)
		if(fileExtension == '.mp3'):
			self.type = self.TYPE_MP3
		elif(fileExtension == '.ogg'):
			self.type = self.TYPE_OGG
