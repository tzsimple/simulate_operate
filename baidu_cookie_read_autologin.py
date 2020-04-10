#读取cookie.txt信息到cookies文件，实现自动登入
from selenium import webdriver
import time
driver= webdriver.Chrome()
driver.get("https://pan.baidu.com/")
time.sleep(5)
fp = open("cookie.txt", "r+", encoding='utf-8')
r = fp.read()
dict = eval(r)          #转换为字典形式
for cookie in dict:  #遍历添加cookie
    if 'expiry' in cookie:
        del cookie['expiry']
    driver.add_cookie(cookie)
time.sleep(5)
driver.get("https://pan.baidu.com/")

