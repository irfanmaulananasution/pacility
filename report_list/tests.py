from django.test import TestCase,Client

# Create your tests here.
class TestReportList(TestCase):

    def test_page_exists(self):
        response = self.client.get('')
        self.assertEquals(response.status_code, 200)

