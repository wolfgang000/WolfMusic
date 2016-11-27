from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from django.test import LiveServerTestCase

class TitleTest(LiveServerTestCase):
	def setUp(self):
		self.browser =  webdriver.Chrome()
		self.browser.implicitly_wait(8)
		
	def tearDown(self):
		self.browser.quit()
		
	def test_check_title(self):
		self.browser.get(self.live_server_url + '/wolfy/mobile')
		self.assertIn('WolfMusic', self.browser.title)
