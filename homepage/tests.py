from django.test import TestCase
from django.urls import resolve
from .views import index

class AnnouncementTestCase(TestCase):
	def test_url_index_exists(self):
		response = self.client.get('/')
		self.assertEqual(response.status_code, 200)

	def test_using_index_function(self):
		found = resolve('/')
		self.assertEqual(found.func, index)

	def test_using_homepage_template(self):
		response = self.client.get('/')
		self.assertTemplateUsed(response, 'homepage/homepage.html')