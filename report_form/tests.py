from django.test import TestCase
from .models import Report
from django.test.client import Client

class ReportTestCase(TestCase):
	# def SetUp(self):
	# 	title1 = "kamar mandi rusak"
	# 	location1 = "balairung"
	# 	time1 = "10:35"
	# 	category1 = "kerusakan"
	# 	description1 = "pintu kamar mandinya gabisa ditutup heu"

	# 	title2 = "kerusakan di pusgiwa"
	# 	location2 = "pusgiwahjjdkdf"
	# 	time2 = "05:11"
	# 	category2 = "sdffdjfsdghshsdj"
	# 	description2 = "jhajads djsfkjsdfksbdf jsdfkjsjdkfs ksdjfkjsdf"

	# 	Report.objects.create(form_title = title1, location = location1, time = time1, category = category1, description = description1)
	# 	Report.objects.create(form_title = title2, location = location2, time = time2, category = category2, description = description2)

	def test_invalid_title(self):
		title = "Reportjadsjdasjkdasjkkajbsdbasddadajdasjkad abjsdjbabjasd jasdjjasdjadsasjdkjbasdjbadsjajskdasjkdasjajhdasjabdjadsjbasdk"
		location = "shfhdsjkfsd"
		time = "10:35"
		category = "my category"
		description = "hauajfahjdfhjsvjsdhfshhgsf"

		report = Report.objects.create(form_title = title, location = location, time = time, category = category, description = description)
		self.assertFalse(report.is_valid_report())

	def test_invalid_location(self):
	    title = "Report"
	    location = "shfhdsjkfsdajsdsajjkadjkdajkadjbksadjbad asjkbjaksfhabsf ajfbkjafajkfkjdfjkkajs ajfbkajfljasf"
	    time = "10:35"
	    category = "my category"
	    description = "hauajfahjdfhjsvjsdhfshhgsf"
	    report = Report.objects.create(form_title = title, location = location, time = time, category = category, description = description)
	    self.assertFalse(report.is_valid_report())

	def test_invalid_category(self):
	    title = "Report"
	    location = "shfh"
	    time = "10:35"
	    category = "mjnsajjdasjkdbjkdsjbasd ajdsjadjkbsabjsabjjsabkdsa ajsdjasjbasbjkdbjskabjakdbjkbjkjbkadsbjkasdbjdsbjasbjk jbksdjbksabjkjasbkdasdasdasd"
	    description = "hauajfahjdfhjsvjsf"
	    report = Report.objects.create(form_title = title, location = location, time = time, category = category, description = description)
	    self.assertFalse(report.is_valid_report())

	def test_index(self):
	    c = Client()
	    response = c.get("/")
	    self.assertEqual(response.status_code, 200)
