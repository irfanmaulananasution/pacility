from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

class PacilityFunctionalTest(TestCase):
	def setUp(self):
		chrome_options = Options()
		chrome_options.add_argument('--dns-prefetch-disable')
		chrome_options.add_argument('--no-sandbox')
		chrome_options.add_argument('--headless')
		chrome_options.add_argument('disable-gpu')

		self.selenium  = webdriver.Chrome('./chromedriver', chrome_options=chrome_options)
		super(PacilityFunctionalTest, self).setUp()

	def tearDown(self):
		self.selenium.quit()
		super(PacilityFunctionalTest, self).tearDown()

	def test_functionality(self):
		selenium = self.selenium
		selenium.get('http://127.0.0.1:8000/report_form')
		time.sleep(3)

		selenium.execute_script("window.scrollTo(0, 500)")
		time.sleep(3)

		username = selenium.find_element_by_id('id_username')
		title = selenium.find_element_by_id('id_title')
		content = selenium.find_element_by_id('id_content')
		button1 = selenium.find_element_by_class_name('btn-submit')

		username.send_keys('tsqfnfl')
		time.sleep(3)
		title.send_keys('Tes Fungsionalitas Homepage')
		time.sleep(3)
		content.send_keys('Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis trud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat la pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.')
		time.sleep(3)
		button1.click()
		time.sleep(3)

		selenium.execute_script("window.scrollTo(0, 500)")
		time.sleep(1)
		selenium.execute_script("window.scrollTo(500, 900)")
		time.sleep(3)

		form_nav = selenium.find_element_by_id('nav-form')
		form_nav.click()
		time.sleep(3)

		title = selenium.find_element_by_id('id_form_title')
		location = selenium.find_element_by_id('id_location')
		time_input = selenium.find_element_by_id('id_time')
		category = selenium.find_element_by_id('id_category')
		description = selenium.find_element_by_id('id_description')
		button2 = selenium.find_element_by_class_name('btn-submit')

		title.send_keys('Kerusakan Meja Kantin')
		time.sleep(3)
		location.send_keys('Kantin Fasilkom')
		time.sleep(3)
		time_input.send_keys('900A')
		time.sleep(3)
		category.send_keys('Fasilkom')
		time.sleep(3)
		description.send_keys('Kaki meja patah, lokasi meja di dekat lorong antara gedung B dan gedung C.')
		time.sleep(3)
		selenium.execute_script("window.scrollTo(0, 500)")
		time.sleep(1)
		button2.click()
		time.sleep(5)
