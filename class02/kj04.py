# coding:utf-8
from selenium import webdriver
from HTMLTestRunner_jpg import HTMLTestRunner
import unittest

class Test(unittest.TestCase):
    def setUp(self):
        print('start')

    def tearDown(self):
        print('end')

    def test_01(self):
        print('111')
        a='abc'
        b='abccd'
    def test_02(self):
        print('222')
        a=3
        b=4
    def test_03(self):
        print('3333')


if __name__=="_main_":
    filename="E:\\testing\\result.html"
    fp=open(filename,"wb")
    runner=HTMLTestRunner(stream=fp,title=u'测试报告',description=u'用例执行情况：')

    runner.run(creatsuite())
    fp.close()
