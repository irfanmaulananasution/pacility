from django.test import TestCase
from django.urls import resolve
from .views import login_view
from django.contrib.auth.models import User

class BaseTestCase(TestCase):
	def setUp(self):
		first_name = 'Louise'
		last_name = 'Banks'
		username = 'louise.banks'
		email = 'louisebanks@arrival.com'
		password = 'arrival'
		new_user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password)
		new_user.save()

	def test_url_login_if_get_method(self):
		response = self.client.get('/base/login')
		self.assertEqual(response.status_code, 302)

	def test_url_login_if_post_and_auth_failed(self):
		response = self.client.post('/base/login', data={'username': 'ian.donnelly', 'password': 'arrival'})
		html_response = response.content.decode('utf8')
		self.assertEqual(response.status_code, 200)
		self.assertIn('Not Found', html_response)

	def test_url_login_if_post_and_auth_success(self):
		response = self.client.post('/base/login', data={'username': 'louise.banks', 'password': 'arrival'})
		html_response = response.content.decode('utf8')
		self.assertEqual(response.status_code, 200)
		self.assertIn('Success', html_response)

	def test_using_login_view_function(self):
		found = resolve('/base/login')
		self.assertEqual(found.func, login_view)
