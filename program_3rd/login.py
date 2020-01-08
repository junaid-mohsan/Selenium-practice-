from selenium import webdriver

import unittest
import time
from pages.loginpage import LoginPage
from pages.registerpage import Registrer
from pages.Dashboard import Dashboard

class McK_login(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome("C:/Drivers/chromedriver_win32/chromedriver.exe")
        self.login = LoginPage(self.driver)
        self.register = Registrer(self.driver)
        self.dashboard = Dashboard(self.driver)
        self.driver.maximize_window()

    def test_login(self):
        self.driver.get("")
        self.assertTrue(self.login.is_browser_on_the_hpage())
        self.driver.find_element_by_link_text('Sign In').click()  

        #Page login  
        self.assertTrue(self.login.is_browser_on_the_loginpage())        
        self.login.enter_username('')              
        self.login.enter_password('')
        self.login.submit_button()
        self.assertTrue(self.dashboard.is_browser_on_the_page())
        self.login.logout()
        
        self.assertTrue(self.register.is_browser_on_the_hpage())
        
        # Page Register    
        self.driver.find_element_by_link_text('Register').click()
        self.assertTrue(self.register.is_browser_on_the_regpage())
        self.register.regemail('')
        self.register.regname('')
        self.register.regusername('')
        self.register.regpassword('')
        self.register.regcountry('')
        self.register.submitButton()
        self.assertTrue(self.dashboard.is_browser_on_the_page())
        self.register.logout()
        self.assertTrue(self.register.is_browser_on_the_hpage())
        
        
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
    