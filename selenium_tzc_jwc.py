#参考https://www.cnblogs.com/lfri/p/10542797.html
#使用selenium，获取html元素
#模拟登陆台州学院教务系统，
# 进入个人课表查询页面
# 选择学年、学期，提交查询

# 模拟登陆台州学院教务系统
from selenium.webdriver.support.select import Select
from selenium import webdriver
from time import sleep

option=webdriver.ChromeOptions()
driver=webdriver.Chrome(options=option)
driver.get("http://www.jwglxt.tzc.edu.cn/jwglxt/xtgl/login_slogin.html")  # 进入台州学院教务登陆页面
sleep(1)
ele_user=driver.find_element_by_id('yhm') #查找元素
ele_pwd=driver.find_element_by_id('mm')
ele_submit=driver.find_element_by_id('dl')
ele_user.send_keys('1998013')
ele_pwd.send_keys('Zhang5221')
ele_submit.click()
sleep(1)
# 获取当前页面url
currentPageUrl = driver.current_url
print("当前页面的url是：", currentPageUrl)

# 进入个人课表查询页面
driver.get("http://www.jwglxt.tzc.edu.cn/jwglxt/kbcx/jskbcx_cxJskbcxIndex.html?gnmkdm=N2150&layout=default&su=1998013")

text_ele = driver.find_element_by_id("xnm_chosen")  # 定位学年下拉框
text_ele.click()  # 点击展开学年下拉列表
sleep(1)
js = "document.getElementById('xnm').style.display='block'" #修改学年下拉列表元素的isDisplayed()值为true
driver.execute_script(js)
select_ele = driver.find_element_by_id("xnm")  # 定位学年下拉框

# Select(select_ele).select_by_index(2)  # 选中选项-3间(索引从0开始)
# Select(select_ele).select_by_value(3)  # 选中选项-3间，value=3
# Select(select_ele).select_by_visible_text("2018-2019")  # 选中-3间，文本"3间"
# # 获取选中的选项
# for select in Select(select_ele).all_selected_options:
#     print("选中选项:", select.text)

for select in Select(select_ele).options:# 获取所有下拉列表选项
    if '2019-' in select.text:
        Select(select_ele).select_by_visible_text(select.text)
sleep(1)

js = "document.getElementById('xqm').style.display='block'" #修改学年下拉列表元素的isDisplayed()值为true
driver.execute_script(js)
select_ele = driver.find_element_by_id("xqm")  # 定位学期下拉框
Select(select_ele).select_by_visible_text("1")  # 选中-3间，文本"3间"
sleep(1)

Btn=driver.find_element_by_id('search_go') #查找查询元素
Btn.click()
