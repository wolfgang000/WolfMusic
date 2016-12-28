from django.test import TestCase
from django.conf import settings
from ...entities.track import file, Track
from ...use_cases.use_case import UseCases

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

class UseCasesTests(TestCase):

	def test_everything(self):
		path = os.path.join(settings.BASE_DIR, 'wolf_services/test/resource/mp3/fake_album/track1.mp3')

		with open(path,'rb') as f:
			content = f.read()
		
		use_cases = UseCases(None)
		track = use_cases.add_track(content,'.mp3')
		self.assertEqual(track,Track(title='Track 1',track_number=1))

