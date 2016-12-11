from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from django.test import LiveServerTestCase
from django.contrib.staticfiles.testing import StaticLiveServerTestCase

class TitleTest(LiveServerTestCase):
	def setUp(self):
		self.browser =  webdriver.Chrome()
		self.browser.implicitly_wait(8)
		
	def tearDown(self):
		self.browser.quit()
		
	def test_check_title(self):
		self.browser.get(self.live_server_url + '/wolfy/mobile')
		self.assertIn('WolfMusic', self.browser.title)


class VoluneControlTest(StaticLiveServerTestCase):
	def setUp(self):
		self.browser =  webdriver.Chrome()
		self.browser.implicitly_wait(8)
		
	def tearDown(self):
		self.browser.quit()
	
	def test_volume_up_slider(self):
		self.browser.get(self.live_server_url + '/wolfy/mobile')
		volume_button = self.browser.find_element_by_class_name('volume-button')
		slider = self.browser.find_element_by_id('slider-vertical')
		
		self.assertFalse(slider.is_displayed())
		volume_button.click()
		self.assertTrue(slider.is_displayed())
		action_chains = ActionChains(self.browser)
		action_chains.drag_and_drop_by_offset(slider, 30, 0).perform()
		audio_tag = self.browser.find_element_by_id('player')
		current_volume = audio_tag.get_attribute('volume')
		self.assertEqual(float(current_volume), 0.8)

