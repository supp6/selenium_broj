# coding=utf-8
from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get("http://www.cnblogs.com/yoyoketang/")
# 滚动条拉到底部
js1= "document.documentElement.scrollTop=10000"
#js11= "window.scrollTo(0,5000);"
#js111 = "window.scrollTo(0,document.body.scrollHeight)"    # 通过计算滚动条高度函数
driver.execute_script(js1)
time.sleep(4)

js2= "document.documentElement.scrollTop=0"    # 回到顶部
#js22 = "window.scrollTo(0,0);"
js222= "window."
driver.execute_script(js2)

# 横向进度
time.sleep(3)
js3= "window.scrollTo(100,0)"
driver.execute_script(js)