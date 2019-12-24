from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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


        self.assertTrue(self.register.is_browser_on_the_hpage())
        
        #Page Register    
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
    