# coding=utf-8
from selenium import webdriver
# Jquery 操作富文本
driver=webdriver.Firefox()
driver.get("https://passport.cnblogs.com/user/signin")
driver.implicitly_wait(20)

username="$('#input1')".val('上海-悠悠')
driver.execute_script(username)

psw= "$('input2').val('yoyo')"
driver.execute_script(psw)

# 点击登录按钮
button ="$('#signin').click()"
driver.execute_script(button)