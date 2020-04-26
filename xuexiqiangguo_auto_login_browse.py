# coding:utf-8
from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import datetime
import random
"""
# 自动浏览学习强国，#读取cookie.txt信息到cookies文件，实现自动登入
# 学习强国，参考
#https://www.pianshen.com/article/5183218678/
#https://www.cnblogs.com/yoyoketang/p/6557421.html
"""


def beforeday(today):
    """
    获取昨天的日期
    :return:
    """
    oneday = datetime.timedelta(days=1)
    yesterday = today-oneday
    return yesterday


def browsenews():
    """
    浏览重要新闻
    :return:
    """
    url = 'https://www.xuexi.cn/98d5ae483720f701144e4dabf99a4a34/5957f69bffab66811b99940516ec8784.html' #重要新闻
    driver = webdriver.Chrome()
    driver.get("https://www.xuexi.cn/")
    time.sleep(5)
    # 判断页面是否正常打开
    while driver.title != '学习强国':
        print("不能访问 https://www.xuexi.cn/")
        time.sleep(60)
        driver.get("https://www.xuexi.cn/")

    # 读取 cookie文件
    fread = open("cookie_xuexi.txt", "r+", encoding='utf-8')
    r = fread.read()
    dict = eval(r)       #转换为字典形式
    for cookie in dict:  #遍历添加cookie
        if 'expiry' in cookie:
            del cookie['expiry']
        driver.add_cookie(cookie)
    time.sleep(5)
    fread.close()
    driver.get(url)  # 进入重要新闻页面
    # 10秒钟内只要找到了元素就开始执行，10秒钟后未找到，就超时； 如果不等待，下面的语句会出现找不到元素的错误
    driver.implicitly_wait(10)
    ele_news=driver.find_elements_by_class_name("text-wrap") #查找元素
    for i in range(6):
        print('浏览第'+str(i)+'条新闻')
        selnews = ele_news[i]
        selnews.click()
        time.sleep(2)
        driver.switch_to.window(driver.window_handles[1])#跳转到新页面
        time.sleep(3)
        for i in range(20):  #向下滚动
            driver.execute_script("window.scrollBy(0, 200)")
            delaysecond = random.randint(5, 10)
            time.sleep(delaysecond)
        for i in range(10):  #向上滚动
            driver.execute_script("window.scrollBy(0, -400)")
            time.sleep(2.5)
        driver.close()  #关闭当前窗口
        driver.switch_to.window(driver.window_handles[0])#回到第一个页面
    driver.quit()  # 退出相关驱动程序,并关闭所有窗口


def browseCCTVNews():
    """
    浏览新闻联播
    :return:
    """
    driver = webdriver.Chrome()
    driver.get("https://www.xuexi.cn/")
    time.sleep(5)
    # 判断页面是否正常打开
    while driver.title != '学习强国':
        print("不能访问 https://www.xuexi.cn/")
        time.sleep(60)
        driver.get("https://www.xuexi.cn/")

    # 读取 cookie文件
    fread = open("cookie_xuexi.txt", "r+", encoding='utf-8')
    r = fread.read()
    dict = eval(r)  # 转换为字典形式
    for cookie in dict:  # 遍历添加cookie
        if 'expiry' in cookie:
            del cookie['expiry']
        driver.add_cookie(cookie)
    time.sleep(5)
    fread.close()
    # 学习电视台,第一频道,新闻联播
    url = 'https://www.xuexi.cn/8e35a343fca20ee32c79d67e35dfca90/7f9f27c65e84e71e1b7189b7132b4710.html?p1='
    today = datetime.date.today()
    for i in range(6):
        print('浏览第'+str(i)+'条新闻联播')
        today = beforeday(today)  #取前一天
        urlnews = url+str(today)
        driver.get(urlnews)  # 进入 前一天的新闻联播 页面
        # 10秒钟内只要找到了元素就开始执行，10秒钟后未找到，就超时； 如果不等待，下面的语句会出现找不到元素的错误
        driver.implicitly_wait(10)
        ele_news = driver.find_element_by_class_name("outter")  # 查找 播放按钮
        ele_news.click()
        time.sleep(200)
    driver.quit()  # 退出相关驱动程序,并关闭所有窗口


def updateCookie():
    """
    # 更新cookie
    :return:
    """
    print('开始更新cookie时间:%s' % (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
    driver = webdriver.Chrome()
    driver.get("https://www.xuexi.cn/")
    # 判断页面是否正常打开
    while driver.title != '学习强国':
        print("不能访问 https://www.xuexi.cn/")
        time.sleep(60)
        driver.get("https://www.xuexi.cn/")

    time.sleep(5)
    # 读取 cookie文件
    fread = open("cookie_xuexi.txt", "r+", encoding='utf-8')
    r = fread.read()
    dict = eval(r)  # 转换为字典形式
    for cookie in dict:  # 遍历添加cookie
        if 'expiry' in cookie:
            del cookie['expiry']
        driver.add_cookie(cookie)
    fread.close()
    driver.get("https://www.xuexi.cn/")
    time.sleep(5)
    loginele = driver.find_elements_by_class_name("logged-link")
    if len(loginele) == 0:
        print("cookie已经过期")
    else:
        print("使用cookie成功登录")
        # 更新 cookie文件
        cookie = driver.get_cookies()  # 获取cookie,列表形式
        f = open("cookie_xuexi.txt", "w")
        f.write(str(cookie))  # 转换为字符串
        time.sleep(10)
        f.close()
        print("cookie文件已经更新")
    print("-----------------------")
    driver.quit()  # 退出相关驱动程序,并关闭所有窗口

def PerformBrowse():
    """
    # 每天15时执行一次任务
    :return:
    """
    delay = 1 * 60 * 60  # 间隔时间1小时。
    while True:
        i = datetime.datetime.now()
        if (i.hour >= 15 and i.hour < 16):
            print('开始浏览:%s......' % (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
            browsenews()
            browseCCTVNews()
        elif (i.hour >= 7 and i.hour < 8) or  (i.hour >= 15 and i.hour < 16) \
                or (i.hour >= 23) or (i.hour>=0 and i.hour<1):
            updateCookie()  # 更新cookie
        time.sleep(delay)


if __name__ == "__main__":
    PerformBrowse()


