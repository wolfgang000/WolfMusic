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
	"""
	Test Volume events, the slider and the volume button
	"""

	def setUp(self):
		self.browser = webdriver.Chrome()
		self.browser.implicitly_wait(8)

	def tearDown(self):
		self.browser.quit()

	def test_volume_up_slider(self):
		self.browser.get(self.live_server_url + '/wolfy/mobile')
		volume_button = self.browser.find_element_by_class_name('volume-button')
		slider = self.browser.find_element_by_id('slider-vertical')

		#Test if slider is hide and press buttom to make it visible
		self.assertFalse(slider.is_displayed())
		volume_button.click()

		#Test if slider is visible
		self.assertTrue(slider.is_displayed())

		#Turn up volume by 25%, default value is 50%
		height = slider.size['height']
		move = ActionChains(self.browser)
		move.click_and_hold(slider).move_by_offset(0, -25 * height / 100).release().perform()

		#Test if current volume is 75% with and error of ~8%
		audio_tag = self.browser.find_element_by_id('player')
		current_volume = audio_tag.get_attribute('volume')
		self.assertAlmostEqual(float(current_volume), 0.75, delta=0.08)

