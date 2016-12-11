from selenium import webdriver
from selenium.webdriver import ActionChains
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


class VoluneControlTest(LiveServerTestCase):
	def setUp(self):
		self.browser =  webdriver.Chrome()
		self.browser.implicitly_wait(8)
		
	def tearDown(self):
		self.browser.quit()
		
	def test_check_title(self):
		self.browser.get(self.live_server_url + '/wolfy/mobile')
		self.assertIn('WolfMusic', self.browser.title)
	
	def test_volume_up_slider(self):
		self.browser.get(self.live_server_url + '/wolfy/mobile')
		volume_button = self.browser.find_element_by_class_name('volume-button')
		volume_button.click()
		slider = self.browser.find_element_by_id('slider-vertical')
		action_chains = ActionChains(self.browser)
		action_chains.drag_and_drop(slider, 30,0).perform()

