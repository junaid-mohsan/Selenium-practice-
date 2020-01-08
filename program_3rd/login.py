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
        self.driver.get("https://courses.edx.org")
        self.assertTrue(self.login.is_browser_on_the_hpage())
        self.driver.find_element_by_link_text('Sign In').click()  

        #Page login  
        self.assertTrue(self.login.is_browser_on_the_loginpage())        
        self.login.enter_username('junaid.mohsan@arbisoft.com')              
        self.login.enter_password('Edx123@#')
        self.login.submit_button()
        self.assertTrue(self.dashboard.is_browser_on_the_page())
        self.login.logout()
        time.sleep(4)


        self.assertTrue(self.register.is_browser_on_the_hpage())
        
        # Page Register    
        # self.driver.find_element_by_link_text('Register').click()
        # self.assertTrue(self.register.is_browser_on_the_regpage())
        # self.register.regemail('zeezddd12@yopmail.com')
        # self.register.regname('zeedd')
        # self.register.regusername('zeeddzzz1')
        # self.register.regpassword('Gillgill12!@')
        # self.register.regcountry('Pakistan')
        # self.register.submitButton()
        # self.assertTrue(self.dashboard.is_browser_on_the_page())
        # self.register.logout()
        # self.assertTrue(self.register.is_browser_on_the_hpage())
        
        
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
    