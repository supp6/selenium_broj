# coding=utf-8
import unittest
from selenium import webdriver
import time


def maillogin(driver,username,psw):
        driver.find_element_by_xpath("//*[@id='switcher_plogin']").click()        #账号登录
        time.sleep(1)
        driver.find_element_by_xpath("//*[@id='u']").send_keys("username")  #点用户名登录
        driver.find_element_by_xpath("//*[@id='p']").send_keys("psw")      ##密码
        driver.find_element_by_xpath("//*[@id='login_button']").click()
        time.sleep(4)





