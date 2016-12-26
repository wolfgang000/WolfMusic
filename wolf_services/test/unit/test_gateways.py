from django.test import TestCase
from django.conf import settings
from ...gateways.track import TrackBaseRepository

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
class TrackBaseRepositoryTests(TestCase):
	def test_abstract_instantiation(self):
		with self.assertRaises(Exception) as context:
			TrackBaseRepository()
		self.assertTrue('Can\'t instantiate abstract class' in str(context.exception))

