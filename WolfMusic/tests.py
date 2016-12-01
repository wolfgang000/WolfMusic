from django.test import TestCase
from django.test import Client
from django.urls import reverse
from django.core.files import File
from rest_framework.test import APIClient
from rest_framework import status
import codecs
import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))



class SwaggerAPITests(TestCase):
	def test_get(self):
		response = self.client.get(reverse('swagger.list'))
		self.assertEqual(response.status_code, status.HTTP_200_OK)
