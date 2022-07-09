'''
@file: test_login.py
@author: 张福卫
@date : 2022/7/6
'''



from selenium import webdriver
from time  import sleep
#添加Chrome相关配置
options = webdriver.ChromeOptions()

# options.add_experimental_option('mobileEmulation',{'deviceName':'iPhone X'})

driver = webdriver.Chrome(chrome_options=options)
# =>打开浏览器时加入配置
driver.get("http://127.0.0.1:81/zentao/user-login.html?tid=af1gpmzc")
# driver.get("http://self-yrcfqdxmhddev.self-yrcfqdxmhddev.paas.test/weather/#/")
#观察一下
sleep(100)
driver.quit()