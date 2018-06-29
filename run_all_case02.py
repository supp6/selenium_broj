# coding=utf-8
from common.HTMLRunner import HTMLTestRunner
import unittest
import time

def all_case():
    case_dir='E:\\testing\\projeb02\\case\\jiekou'
    rule='test*.py'
    discover=unittest.defaultTestLoader.discover(case_dir,rule)
    print(discover)
    return discover

if __name__ =="__main__":
    t=time.strftime('%Y_%m_%d %H_%M_%S')
    rpfile="E:\\testing\\projeb02\\report\\"+ t + "result.html"
    fp=open(rpfile,"wb")
    runner=HTMLTestRunner(fp,title='报告标题：这是我的接口测试报告',description="报告内容如下：",retry=1,verbosity=2)

    runner.run(all_case())
    fp.close()


