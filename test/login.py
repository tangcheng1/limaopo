# coding=utf-8
import unittest
from po import DashPage
from po import LoginFeng
class LoginTestLimao(unittest.TestCase):
    def setUp(self):
#         DashPage.Dash().click_kaijigg()
#         DashPage.Dash().click_jinrugg()
#         DashPage.Dash().click_notice()
#         DashPage.Dash().click_notice()
        LoginFeng.U().kaiji()
        DashPage.Dash().login()                               
    def test_login(self): 
        DashPage.Dash().click_me()  
        self.assertEqual(DashPage.Dash().duanyanlogin(),'18702766541')
    def tearDown(self):
        DashPage.Dash().quit()
if __name__ == "__main__":
    unittest.main()