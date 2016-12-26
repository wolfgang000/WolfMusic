from django.test import TestCase
from django.conf import settings
from django.core.urlresolvers import reverse

import os
from ...serializer.track import TrackSerializer
from ...entities.track import Track

class TrackSerializerTests(TestCase):

	def test_instantiation(self):
		track = Track(title='ranchera', track_number=1, id=1)
		serializer = TrackSerializer(track)
		self.assertDictEqual(
								{'title': 'ranchera', 'track_number': 1, 'id': 1, 'url' : reverse('track.detail', args=[str(1)])},
								serializer.data
							)