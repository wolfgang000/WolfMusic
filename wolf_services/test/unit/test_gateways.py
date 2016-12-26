from django.test import TestCase
from django.conf import settings
import os
from ...gateways.track import TrackBaseRepository, TrackDjangoOrmRepository
from ...entities.track import Track

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

class TrackBaseRepositoryTests(TestCase):
	def test_abstract_instantiation(self):
		with self.assertRaises(Exception) as context:
			TrackBaseRepository()
		self.assertTrue('Can\'t instantiate abstract class' in str(context.exception))

class TrackDjangoOrmRepositoryTests(TestCase):
	
	def test_instantiation(self):
		track_repository = TrackDjangoOrmRepository()
		self.assertTrue(issubclass( TrackDjangoOrmRepository, TrackBaseRepository))
	
	def test_add_and_get(self):
		track_repository = TrackDjangoOrmRepository()
		track = Track(title='ranchera', track_number=1)
		track = track_repository.add(track)
		
		self.assertIsNotNone(track)
		self.assertIsNotNone(track.id)

		track_intance = track_repository.get(id=track.id)

		self.assertIsNotNone(track_intance)

		self.assertEquals(track.id, track_intance.id)
		self.assertEquals(track.title, track_intance.title)

