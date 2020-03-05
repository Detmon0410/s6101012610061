from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from django.test import LiveServerTestCase


class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_visit_web_and_calculate(self):
        # Ana Want to calculate number she visit my website
        self.browser.get(self.live_server_url)
        time.sleep(5)

        pose_btn = self.browser.find_element_by_id('POSEMODE')
        pose_btn.click()

        time.sleep(3)

        # She saw that the title of this website is Calculator
        self.assertIn('Calculator POSE', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Welcome to the best Calculator app', header_text)

        # she type first value is 50 in text box
        var_x = self.browser.find_element_by_name('X')
        var_x.send_keys('50')
        time.sleep(3)

        # she type second value is 100 in next text box
        var_y = self.browser.find_element_by_name('Y')
        var_y.send_keys('100')
        time.sleep(3)

        # she press plus button for calculate
        plus_btn = self.browser.find_element_by_name('plus-submit')
        plus_btn.click()
        time.sleep(3)

        # she saw the result on result label
        result = self.browser.find_element_by_id('lb01').text
        self.assertIn('Result is : 150', result)
        time.sleep(3)
        # she looking at calculate log
        cal_log = self.browser.find_element_by_id('result_logs').text
        self.assertIn('50+100=150', cal_log)
        time.sleep(3)

        # she type first value is 450 in text box
        var_x = self.browser.find_element_by_name('X')
        var_x.send_keys('450')
        time.sleep(3)

        # she type second value is 100 in next text box
        var_y = self.browser.find_element_by_name('Y')
        var_y.send_keys('100')
        time.sleep(3)

        # she press minus button for calculate
        minus_btn = self.browser.find_element_by_name('minus-submit')
        minus_btn.click()
        time.sleep(3)

        # she saw the result on result label
        result = self.browser.find_element_by_name('result_label').text
        self.assertIn('Result is : 350', result)
        time.sleep(3)

        # she look at calculate log
        cal_log = self.browser.find_element_by_id('result_logs').text
        self.assertIn('50+100=150\n450-100=350', cal_log)
        time.sleep(3)

        # she type first value is 50 in text box
        var_x = self.browser.find_element_by_name('X')
        var_x.send_keys('3')
        time.sleep(3)

        # she type second value is 100 in next text box
        var_y = self.browser.find_element_by_name('Y')
        var_y.send_keys('3')
        time.sleep(3)

        # she press multiply button for calculate
        plus_btn = self.browser.find_element_by_name('multiply-submit')
        plus_btn.click()
        time.sleep(3)

        # she saw the result on result label
        result = self.browser.find_element_by_id('lb01').text
        self.assertIn('Result is : 9', result)
        time.sleep(3)
        # she looking at calculate log
        cal_log = self.browser.find_element_by_id('result_logs').text
        self.assertIn('50+100=150\n450-100=350\n3*3=9', cal_log)
        time.sleep(3)

        # she type first value is 450 in text box
        var_x = self.browser.find_element_by_name('X')
        var_x.send_keys('500')
        time.sleep(3)

        # she type second value is 100 in next text box
        var_y = self.browser.find_element_by_name('Y')
        var_y.send_keys('2')
        time.sleep(3)

        # she press minus button for calculate
        minus_btn = self.browser.find_element_by_name('divide-submit')
        minus_btn.click()
        time.sleep(3)

        # she saw the result on result label
        result = self.browser.find_element_by_name('result_label').text
        self.assertIn('Result is : 250', result)
        time.sleep(3)

        # she look at calculate log
        cal_log = self.browser.find_element_by_id('result_logs').text
        self.assertIn('50+100=150\n450-100=350\n3*3=9\n500/2=250', cal_log)
        time.sleep(3)
