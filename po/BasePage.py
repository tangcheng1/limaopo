#-*- coding: utf-8 -*-
from selenium.webdriver.support.ui import WebDriverWait
from appium import webdriver
import driver
class Base:
    driver = driver.APPiumTest().get_driver()     
    
#重新封装单个元素定位方法
    def find_element(self,loc):
        try:
            WebDriverWait(self.driver,15).until(lambda driver:driver.find_element(*loc).is_displayed())
            return self.driver.find_element(*loc)
        except:
            print u"%s 页面中未能找到 %s 元素" %(self,loc)

#重新封装一组元素定位方法
    def find_elements(self,loc):
        try:
            if len(self.driver.find_elements(*loc)):
                return self.driver.find_elements(*loc)
        except:
            print u"%s 页面中未能找到 %s 元素" %(self,loc)
    #重写定义send_keys方法
    def send_keys(self,loc,value,clear_first=True,click_first=True):
        try:
            if click_first:
                self.find_element(loc).click()
            if clear_first:
                self.find_element(loc).clear()
            self.find_element(loc).send_keys(value)
        except AttributeError:
            print "%s 页面未能找到 %s 元素" %(self,loc)
#重新封装按钮点击方法
    def clickButton(self,loc,find_first=True):
        try:
            if find_first:
                self.find_element(loc)
            self.find_element(loc).click()
        except AttributeError:
            print "%s 页面未能找到 %s 按钮" %(self,loc)
            
#     #重写switch_frame方法
#     def switch_frame(self, loc):
#         return self.driver.switch_to_frame(loc)
#         #定义open方法，调用_open()进行打开链接
#     
#     def open(self):
#         self._open(self.base_url, self.pagetitle)
#     
#     #使用current_url获取当前窗口Url地址，进行与配置地址作比较，返回比较结果（True False）
#     def on_page(self, pagetitle):
#         return pagetitle in self.driver.title
#     
#     #定义script方法，用于执行js脚本，范围执行结果
#     def script(self, src):
#         self.driver.execute_script(src)
#     
