# 学习强国,#手动登录获取cookies，把cookies信息保存到cookie.txt
# coding:utf-8
from selenium import webdriver
import time

def login():
    # 手动登录获取cookies
    driver = webdriver.Chrome()
    driver.get("https://pc.xuexi.cn/points/login.html")
    time.sleep(20)  # 留充足的时间手动输入账号密码
    driver.get("https://www.xuexi.cn/")#必须重新打开一次，否则cookie不能写入到文件
    cookie = driver.get_cookies()  # 获取cookie,列表形式
    f = open("cookie_xuexi.txt", "w")
    f.write(str(cookie))  # 转换为字符串
    f.close()
    print(cookie)
    print(driver.title)

if __name__ == "__main__":
    login()
