from django.db import models

class Announcement(models.Model):
	username = models.CharField(max_length = 20)
	initial = models.CharField(max_length = 1)
	title = models.CharField(max_length = 50)
	content = models.TextField()
	date = models.CharField(max_length = 30)
	time = models.CharField(max_length = 5)

	def is_valid_announcement(self):
		username_valid = len(self.username) > 0 and len(self.username) < 21
		initial_valid = self.initial == self.username[:1].upper()
		title_valid = len(self.title) > 0 and len(self.title) < 51
		content_valid = len(self.content) > 0

		return username_valid and initial_valid and title_valid and content_valid

	
	def __str__(self):
		return f"{self.date} - {self.title}"