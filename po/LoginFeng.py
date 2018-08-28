#coding=utf-8
from appium import webdriver
from selenium.webdriver.common.by import By
import DashPage

class U(DashPage.Dash):

    def kaiji(self):       
        DashPage.Dash().click_kaijigg()         
        DashPage.Dash().click_jinrugg() 
        DashPage.Dash().click_notice() 
        DashPage.Dash().click_notice()      
    

