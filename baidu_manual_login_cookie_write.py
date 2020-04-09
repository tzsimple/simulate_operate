#手动登录获取cookies，把cookies信息保存到cookie.txt
# coding:utf-8
from selenium import webdriver
import time

def login():
    # 手动登录获取cookies
    driver = webdriver.Chrome()
    driver.get("https://pan.baidu.com/")
    # driver.implicitly_wait(10)  #10秒钟内只要找到了元素就开始执行，10秒钟后未找到，就超时； 如果不等待，下面的语句会出现找不到元素的错误
    time.sleep(20)  # 留充足的时间手动输入账号密码
    driver.get("https://pan.baidu.com/")#必须重新打开一次，否则cookie不能写入到文件
    cookie = driver.get_cookies()  # 获取cookie,列表形式
    f = open("cookie.txt", "w")
    f.write(str(cookie))  # 转换为字符串
    f.close()
    print(cookie)
    print(driver.title)

if __name__ == "__main__":
    login()
