#学习强国，参考
#https://www.cnblogs.com/angle6-liu/p/10580635.html
#https://www.pianshen.com/article/5183218678/

#json文件的解析提取
#https://blog.csdn.net/t8116189520/article/details/78727971


# 模拟浏览学习强国
from selenium.webdriver.support.select import Select
from selenium import webdriver
from time import sleep

url = 'https://www.xuexi.cn/98d5ae483720f701144e4dabf99a4a34/5957f69bffab66811b99940516ec8784.html' #重要新闻
option=webdriver.ChromeOptions()
driver=webdriver.Chrome(options=option)
driver.get('https://www.xuexi.cn/')  # 进入首页
driver.get(url)  # 进入重要新闻页面
sleep(5)

ele_user=driver.find_elements_by_class_name("text-wrap") #查找元素
selu = ele_user[0]
selu.click()
selu = ele_user[1]
selu.click()


def GetCookies(self):       #初次登录用selenium模拟，并获得cookies
         browser = webdriver.Chrome()
         browser.get("https://www.zhihu.com/signin")
         browser.find_element_by_xpath("//main//div[2]/div[1]/form/div[1]/div[2]/div[1]/input").send_keys("13060882373")
         browser.find_element_by_xpath("//main//div[2]/div[1]/form/div[2]/div/div[1]/input").send_keys("xxxxxx")
         browser.find_element_by_xpath("//main//div[2]/div[1]/form/button").click()
         time.sleep(10)
         cookies = browser.get_cookies()
         browser.quit()
         return cookies