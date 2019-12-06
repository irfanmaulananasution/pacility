from django.db import models

class Report(models.Model):
	form_title = models.CharField(max_length = 20)
	location = models.CharField(max_length = 20)
	time = models.TimeField()
	category = models.CharField(max_length = 20)
	description = models.TextField()

	def is_valid_report(self):
	    form_title_valid = len(self.form_title) > 0 and len(self.form_title) < 21
	    location_valid = len(self.location) > 0 and len(self.location) < 21
	    category_valid = len(self.category) > 0 and len(self.category) < 21
	    description_valid = len(self.description) > 0

	    return form_title_valid and location_valid and category_valid and description_valid

	def __str__(self):
	    return f"{self.date} - {self.title}"


