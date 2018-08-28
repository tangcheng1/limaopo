from appium import webdriver

class APPiumTest:
    def __init__(self):
        desired_caps = {
                    'platformName':'Android',
                    'deviceName':'127.0.0.1:62001',
                    'platformVersion':'4.4.2',
                    'appPackage':'com.first.saccelerator',
                    'appActivity':'com.first.saccelerator.ui.activity.CheckPermissionsActivity',
                    'noReset':True}  
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(30)
        
    def get_driver(self):
        return self.driver    