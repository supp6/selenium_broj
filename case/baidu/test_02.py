# coding:utf-8
from selenium import webdriver
import unittest
import time

class Blogin(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Firefox()
        self.driver.get('https://passport.cnblogs.com/user/signin')
        time.sleep(2)

    def test11(self):
        self.driver.find_element_by_xpath("//*[@id='input1']").send_keys("supp6")
        self.driver.find_element_by_id('input2').send_keys('s&545900')
        self.driver.find_element_by_xpath("//*[@id='signin']").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//*[@id='captchaBox']/div/div[3]/span[2]").click()


if __name__ =="__main__":
    unittest.main()





