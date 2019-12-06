from django.test import TestCase
from django.test import Client
from django.urls import resolve
from django.http import HttpRequest
from datetime import date
from . import views
from .forms import TestimonyForm
from .models import Testimony
from django.contrib.auth import get_user_model
import unittest


class TestimonyTest(TestCase):
    def setUp(self):
        Testimony.objects.create(username = "joko", title = "saya suka laporan doi", content = "saya males nulis, pokoknya bagus")
		
        User = get_user_model()
        user = User.objects.create_user('temporary', 'temporary@gmail.com', 'temporary')
		
    def test_announcement_amount(self):
        testimony = Testimony.objects.all()
        self.assertEqual(testimony.count(), 1)
        
    def test_landing_page_response(self):
        self.response = Client().get('/testimony/')
        self.assertEqual(self.response.status_code, 200)

    def test_url_name(self):
        self.found = resolve('/testimony/')
        self.assertEqual(self.found.url_name, 'testimony')

    def test_page_header_is_exist(self):
        self.response = Client().get('/testimony/')
        self.assertIn('TESTIMONY</h1>', self.response.content.decode())

    def test_page_title_is_exist(self):
        self.response = Client().get('/testimony/')
        self.assertIn('<title>Testimony - pacility.</title>', self.response.content.decode())

    def test_testimony_function(self):
        self.found = resolve('/testimony/')
        self.assertEqual(self.found.func, views.testimony)

    def test_calculator_form(self):
        form_data = {
            'username': 'This is a test',
            'title': 'test',
            'content' : 'test content'
        }
        testimony_form = TestimonyForm(data=form_data)
        self.assertTrue(testimony_form.is_valid())

    def test_testimony_form_username_not_valid(self):
        form_data = {
            'username': '',
            'title': 'test',
            'content' : 'test content'
        }
        testimony_form = TestimonyForm(data=form_data)
        self.assertFalse(testimony_form.is_valid())

    def test_testimony_form_title_not_valid(self):
        form_data = {
            'username': 'joko',
            'title': '',
            'content' : 'anu'
        }
        testimony_form = TestimonyForm(data=form_data)
        self.assertFalse(testimony_form.is_valid())

    def test_testimony_form_content_not_valid(self):
        form_data = {
            'username': 'joko',
            'title': 'test',
            'content' : ''
        }
        testimony_form = TestimonyForm(data=form_data)
        self.assertFalse(testimony_form.is_valid())
        
    def test_response_is_posted(self):
        self.response = Client().post('/testimony/', {'username': 'This is a test'})
        self.assertEqual(self.response.status_code, 200)

    def test_profile_url_name(self):
        self.found = resolve('/testimony/')
        self.assertEqual(self.found.url_name, 'testimony')

    def test_template_is_testmiony(self):
        response = Client().get('/testimony/')
        self.assertTemplateUsed(response, 'testimony.html')

	#2 template ini bakal di tampilin dengan 1 url tapi ada if di views nya
    def test_testimony_showed_for_non_authenticated_user(self):
        response = Client().get('/testimony/')
        self.assertIn('<div class="testimony-content"', response.content.decode())
		
    def test_testimony_showed_for_authenticated_user(self):
        c = Client()
        c.login(username='temporary', password='temporary')
		
        response = c.get('/testimony/')
        self.assertIn('<div class="testimony-content"', response.content.decode())

    def test_authenticated_user_template(self):
        c = Client()
        c.login(username='temporary', password='temporary')

        response = Client().get('/testimony/')
        self.assertTemplateUsed(response, 'testimony.html')

    # def test_authenticated_user_template_have_testify_button(self):
    #     c = Client()
    #     c.login(username='temporary', password='temporary')
		
    #     response = Client().get('/testimony/')
    #     self.assertIn('Testify</button>', response.content.decode())
