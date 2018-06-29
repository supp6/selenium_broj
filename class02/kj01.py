#coding-utf-8
from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains

driver=webdriver.Firefox()
driver.get('https://www.baidu.com/')
moves=driver.find_element_by_link_text('设置')
ActionChains(driver).move_to_element(moves).perform()     #鼠标移动到‘设置’
driver.find_element_by_link_text('搜索设置').click()
time.sleep(2)
driver.find_element_by_link_text('保存设置').click()
time.sleep(2)
mas=driver.switch_to_alert()          #切换到提示框
print(mas.text)
mas.accept()

driver.quit()
