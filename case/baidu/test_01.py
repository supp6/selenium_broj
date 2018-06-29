# coding=utf-8
from selenium import webdriver
import unittest
import time


class Baidu(unittest.TestCase):

    def setUp(self):
        self.driver=webdriver.Firefox()
        self.driver.get('https://www.baidu.com')

    def test_aa(self):
        self.driver.find_element_by_css_selector('#kw').send_keys('python')
        self.driver.find_element_by_css_selector('#su').click()
        time.sleep(2)

    def test_bb(self):
        self.driver.find_element_by_css_selector('#kw').send_keys('selenium')
        self.driver.find_element_by_css_selector('#su').click()
        time.sleep(2)
    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()

