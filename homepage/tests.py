from django.test import TestCase
from django.urls import resolve
from .views import index, add_announcement
from .models import Announcement
from .forms import AnnouncementForm

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

	def test_form_in_context(self):
		response = self.client.get('/')
		form = response.context['form']
		self.assertIsInstance(form, AnnouncementForm)

	def test_announcements_in_context(self):
		response = self.client.get('/')
		form = response.context['announcements'].get(id=1)
		self.assertIsInstance(form, Announcement)

	def test_using_homepage_template(self):
		response = self.client.get('/')
		self.assertTemplateUsed(response, 'homepage/homepage.html')

	def test_url_add_announcement_exists(self):
		response = self.client.post("/add_announcement", data = {'username': 'username', 'title': 'announcement title', 'content': 'announcement content'})
		self.assertEqual(response.status_code, 302)

	def test_using_add_announcement_function(self):
		found = resolve("/add_announcement")
		self.assertEqual(found.func, add_announcement)

	def test_redirect_to_index(self):
		response = self.client.post("/add_announcement", data = {'username': 'username', 'title': 'announcement title', 'content': 'announcement content'}, follow=True)
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

	def test_announcement_string_representation(self):
		announcement1 = Announcement.objects.get(id=1)
		announcement2 = Announcement.objects.get(id=2)

		self.assertEqual(str(announcement1), f"{announcement1.date} - {announcement1.title}")
		self.assertEqual(str(announcement2), f"{announcement2.date} - {announcement2.title}")