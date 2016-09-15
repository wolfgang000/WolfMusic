from django.test import TestCase
from django.test import Client
from django.urls import reverse
from .. import models
from django.core.files import File
from rest_framework.test import APIClient
from rest_framework import status
import codecs

import os
from django.test.client import encode_multipart, RequestFactory

BASE_DIR = os.path.dirname(os.path.abspath(__file__))



class TrackViewTests(TestCase):
	def setUp(self):
		self.client =  APIClient()
	
	def _get_form_file(self, path):
		f = open(path, 'rb')
		return {'file': f}
	
	
	def test_post_one_mp3(self):
		data = self._get_form_file(os.path.join(BASE_DIR, 'resource/mp3/empty_metadata.mp3'))
		response = self.client.post(reverse('track.list'),data,format='multipart')
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class AlbumViewTests(TestCase):
	def setUp(self):
		self.client =  APIClient()
		
		path = os.path.join(BASE_DIR, 'resource/mp3/fake_album/track1.mp3')
		auxFile = open(path,'rb')
		file = File(auxFile)
		track1 = models.Track()
		track1.file.save('track1.pm3',file)
		track1.name = 'track1.pm3'
		track1.save()
		track1.updateMetadataSave()
		
		path = os.path.join(BASE_DIR, 'resource/mp3/fake_album/track2.mp3')
		file = File(open(path))
		track2 = models.Track(file = file,name = 'track2.mp3')
		track2.save()
		track2.updateMetadataSave()
		
	
	def test_get(self):
		response = self.client.get(reverse('album.list'))
		self.assertEqual(response.status_code, status.HTTP_200_OK)