from django.test import TestCase
from django.urls import resolve
from .views import index
from .models import Announcement

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

	def test_valid_announcement(self):
		username = "louise.banks"
		initial = "L"
		title = "Announcement1"
		content = "Announcement content goes here..."
		date = "Saturday, 19 October 2019"
		time = "10:35"

		announcement = Announcement.objects.create(username = username, initial = initial, title = title, content = content, date = date, time = time)
		self.assertTrue(announcement.is_valid_announcement())

	def test_invalid_username(self):
		username = "floccinaucinihilipilification"
		initial = "F"
		title = "Announcement"
		content = "Here is the content"
		date = "Saturday, 19 October 2019"
		time = "11:03"

		announcement = Announcement.objects.create(username = username, initial = initial, title = title, content = content, date = date, time = time)
		self.assertFalse(announcement.is_valid_announcement())

	def test_invalid_initial(self):
		username = "louise.banks"
		initial = "R"
		title = "Announcement"
		content = "Here is the content"
		date = "Saturday, 19 October 2019"
		time = "11:03"

		announcement = Announcement.objects.create(username = username, initial = initial, title = title, content = content, date = date, time = time)
		self.assertFalse(announcement.is_valid_announcement())

	def test_invalid_title(self):
		username = "louise.banks"
		initial = "L"
		title = "Floccinaucinihilipilification Floccinaucinihilipilification"
		content = "Here is the content"
		date = "Saturday, 19 October 2019"
		time = "11:03"

		announcement = Announcement.objects.create(username = username, initial = initial, title = title, content = content, date = date, time = time)
		self.assertFalse(announcement.is_valid_announcement())