# -*- coding: utf-8 -*
import pyautogui, time, sys
import pyperclip

#https://www.jb51.net/article/146786.htm
#pyautogui，GUI任务模拟，模拟鼠标键盘操作
#模拟登陆https://sso.tzc.edu.cn/login?service=https%3A%2F%2Fi.tzc.edu.cn%2Fcas%2Fvalidate&sn=undefined

#获得屏幕的分辨率
width, height = pyautogui.size()
print(width,height)

pyautogui.click(1639,400)

x, y,z,h =pyautogui.locateOnScreen('tzclogin.png')#找到该图片对应的屏幕位置
x, y = pyautogui.center((x, y,z,h)) # 获得中心点

#控制鼠标移动
pyautogui.moveTo(x, y-300, duration=1)
pyautogui.click(x, y-300)
pyautogui.typewrite('1998013')
pyautogui.click(1639,400)
pyautogui.moveTo(x, y-180, duration=1)
pyautogui.click(x, y-180)
pyautogui.typewrite('Zhang5221')
pyautogui.click(x,y)

# #键盘输入中文由于pyautogui不支持，所以可以使用pyperclip先复制中文到剪贴板然后使用pyautogui进行ctrl+v即可。
# pyperclip.copy(u'开学')
# pyperclip.paste()
# pyautogui.hotkey('ctrl', 'v')
# time.sleep(1)
