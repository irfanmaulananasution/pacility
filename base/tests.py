from django.test import TestCase
from django.urls import resolve
from .views import login_view, logout_view, register
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

	def test_url_logout_exists(self):
		response = self.client.get('/base/logout')
		self.assertEqual(response.status_code, 302)

	def test_using_logout_view_function(self):
		found = resolve('/base/logout')
		self.assertEqual(found.func, logout_view)

	def test_logout_using_homepage_template(self):
		response = self.client.get('/base/logout', follow=True)
		self.assertTemplateUsed(response, 'homepage/homepage.html')

	def test_url_register_if_get_method(self):
		response = self.client.get('/base/register')
		self.assertEqual(response.status_code, 302)

	def test_url_register_if_post_method(self):
		response = self.client.post('/base/register', data={'first_name': 'Ian', 'last_name': 'Donnelly', 'username': 'ian.donnelly', 'email': 'iandonnelly@arrival.com', 'password': 'arrival'})
		self.assertEqual(response.status_code, 302)

	def test_using_register_view_function(self):
		found = resolve('/base/register')
		self.assertEqual(found.func, register)

	def test_register_using_homepage_template(self):
		response = self.client.post('/base/register', data={'first_name': 'Ian', 'last_name': 'Donnelly', 'username': 'ian.donnelly', 'email': 'iandonnelly@arrival.com', 'password': 'theoreticalphysicist'}, follow=True)
		self.assertTemplateUsed(response, 'homepage/homepage.html')