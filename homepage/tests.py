from django.test import TestCase
from django.urls import resolve
from .views import index
from .models import Announcement

class AnnouncementTestCase(TestCase):
	def setUp(self):
		username1 = "louise.banks"
		initial1 = "L"
		title1 = "Announcement1"
		content1 = "Announcement content goes here..."
		date1 = "Saturday, 19 October 2019"
		time1 = "10:35"

		username2 = "ian.donnelly"
		initial2 = "I"
		title2 = "Announcement2"
		content2 = "Another announcement content..."
		date2 = "Saturday, 19 October 2019"
		time2 = "18:43"

		Announcement.objects.create(username = username1, initial = initial1, title = title1, content = content1, date = date1, time = time1)
		Announcement.objects.create(username = username2, initial = initial2, title = title2, content = content2, date = date2, time = time2)

	def test_url_index_exists(self):
		response = self.client.get('/')
		self.assertEqual(response.status_code, 200)

	def test_using_index_function(self):
		found = resolve('/')
		self.assertEqual(found.func, index)

	def test_using_homepage_template(self):
		response = self.client.get('/')
		self.assertTemplateUsed(response, 'homepage/homepage.html')

	def test_announcement_count(self):
		announcements = Announcement.objects.all()
		self.assertEqual(announcements.count(), 2)

	def test_valid_announcement(self):
		announcement1 = Announcement.objects.get(id=1)
		announcement2 = Announcement.objects.get(id=2)

		self.assertTrue(announcement1.is_valid_announcement())
		self.assertTrue(announcement2.is_valid_announcement())
	
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

