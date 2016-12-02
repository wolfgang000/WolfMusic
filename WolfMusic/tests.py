from django.test import TestCase
from django.urls import reverse
from rest_framework import status

class SwaggerAPITests(TestCase):
	def test_get(self):
		response = self.client.get(reverse('swagger.list'))
		self.assertEqual(response.status_code, status.HTTP_200_OK)
