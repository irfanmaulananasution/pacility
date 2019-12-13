from django.test import TestCase,Client

# Create your tests here.
class TestReportList(TestCase):

    def test_page_exists(self):
        response = self.client.get('')
        self.assertEquals(response.status_code, 200)

    def test_page_dont_exist(self):
        response = self.client.get('/unavailable')
        self.assertEquals(response.status_code, 404)

    def test_if_index_used_the_right_template(self):
        response = Client().get('/report_list/')
        self.assertTemplateUsed(response, 'report_list/report_list.html')

    

