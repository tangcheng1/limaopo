#coding=utf-8

from selenium.webdriver.common.by import By
import BasePage

class Dash(BasePage.Base):
    #开机广告
    kaijigg_loc = (By.ID,"com.first.saccelerator:id/ij")
    #进入广告
    jinrugg_loc = (By.ID,"com.first.saccelerator:id/ni")
    #升级&公告    
    notice_loc = (By.ID,"com.first.saccelerator:id/nf")
    #我的 
    notice_loc = (By.ID,"com.first.saccelerator:id/nf")
  
    #点击开机广告
    def click_kaijigg(self):
        self.clickButton(self.kaijigg_loc)
    #点击进入广告
    def click_jinrugg(self):
        self.clickButton(self.jinrugg_loc)
    #点击升级和公告  
    def click_notice(self):
        self.clickButton(self.notice_loc)

  

 
    #调用send_keys对象，输入用户名
#     def input_username(self, username):
#         self.find_element(*self.username_loc).send_keys(username)
#     #调用send_keys对象，输入密码
#     def input_password(self, password):
#         self.find_element(*self.password_loc).send_keys(password)
#     #调用send_keys对象，点击登录
#     def click_submit(self):
#         self.find_element(*self.submit_loc).click()
#     #用户名或密码不合理是Tip框内容展示
#     def show_span(self):
#         return self.find_element(*self.span_loc).text
#     #切换登录模式为动态密码登录（IE下有效）
#     def swich_DynPw(self):
#         self.find_element(*self.dynpw_loc).click()
#     #登录成功页面中的用户ID查找
#     def show_userid(self):
#         return self.find_element(*self.userid_loc).text


    


    def login(self):
        driver=self.driver
        #进入首页后点击‘我的’按钮
        driver.find_element_by_id('com.first.saccelerator:id/gf').click()    
        # 点击登录头像按钮，进行登录，跳转到登录界面
        driver.find_element_by_id('com.first.saccelerator:id/lv').click() 
        # 输入用户名
        driver.find_element_by_id('com.first.saccelerator:id/fy').clear()
        driver.find_element_by_id('com.first.saccelerator:id/fy').send_keys('18702766541')
        driver.hide_keyboard()  #隐藏输入法
        driver.find_element_by_id('com.first.saccelerator:id/g1').clear()
        # 输入密码
        driver.find_element_by_id('com.first.saccelerator:id/g1').send_keys('654321')
        driver.hide_keyboard() #隐藏输入法
        # 点击确认登录按钮
        driver.find_element_by_id('com.first.saccelerator:id/g2').click() 
     
    def click_me(self): 
        driver=self.driver
        driver.find_element_by_id('com.first.saccelerator:id/gf').click()  
          
    def duanyanlogin(self):
        driver=self.driver        
        ele=driver.find_element_by_id('com.first.saccelerator:id/kw').text
        return ele     
          
    def quit(self):
        driver=self.driver
        driver.quit()



