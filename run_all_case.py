# coding:utf-8
import unittest
from common.HTMLRunner import HTMLTestRunner
import time


# 待执行用例的目录
case_dir="E:\\testing\\case\\baidu"
discover = unittest.defaultTestLoader.discover(case_dir, pattern="test*.py",top_level_dir=None)


if __name__ == '__main__':
    now=time.strftime("%Y-%m-%d %H-%M-%S")
    reportfile = "E:\\testing\\report\\"+now+  "result.html"
    fp = open(reportfile, "wb")
    runner=HTMLTestRunner(fp,
                          verbosity=2,
                          title="自动化测试报告",
                          description="用例执行情况")

    runner.run(discover)
    fp.close()


