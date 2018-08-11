#coding=utf-8
from selenium import webdriver
import time
driver = webdriver.Firefox()

driver.maximize_window()  # 最大化浏览器窗口
driver.implicitly_wait(8)  # 设置隐式时间等待

driver.get("https://www.baidu.com")  # 地址栏输入百度地址
driver.find_element_by_xpath("//*[@id='kw']").send_keys("selenium")  # 搜索输入框输入Selenium
driver.find_element_by_xpath("//*[@id='su']").click()  # 点击百度一下按钮

print ('Browser will be closed')
driver.quit()
print ('Browser is close')
