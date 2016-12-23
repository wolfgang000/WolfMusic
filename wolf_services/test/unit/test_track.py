from django.test import TestCase
from django.conf import settings
from ...entities.track import file, Track

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

class FileTests(TestCase):

	def test_everything(self):
		t_file = file()
		path = os.path.join(settings.BASE_DIR, 'resources/tests/low_quality_mp3/Movie_On_The_Moon/01-Sono_Tranquile.mp3')
		t_file.path = path
		
		
		self.assertEqual(t_file.path, path)

		with open(path,'rb') as f:
			content = f.read()

		self.assertEqual(t_file.read(), content)
