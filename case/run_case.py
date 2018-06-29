# coding=utf-8
import unittest
from selenium import webdriver
from case.baidu.login import maillogin
import time



class TestLogin(unittest.TestCase):

    def setUp(self):
        self.driver=webdriver.Firefox()
        self.driver.get("https://mail.qq.com/")
        time.sleep(4)

    def test_maillogin(self):
        ##调用登录函数
        maillogin(self.driver,"736837612@qq.com",'197499119')
        time.sleep(3)




    def tearDown(self):
        self.driver.quit()



if __name__ == '__main__':
    unittest.main()
