from django.db import models

class Testimony(models.Model):
	username = models.CharField(max_length = 20)
	title = models.CharField(max_length = 50)
	content = models.TextField()
	
	def __str__(self):
		return f"{self.title}"
