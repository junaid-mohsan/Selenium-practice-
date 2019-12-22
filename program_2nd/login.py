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
        # self.driver.get("")
        # self.register.regemail('')
        # self.register.regname('')
        # self.register.regusername('')
        # self.register.regpassword('')
        # self.register.regcountry('')
        # self.register.submitButton()

        # time.sleep(5)
        self.driver.get("https://courses.edx.org/login")
        self.login.enter_username('junaid.mohsan@arbisoft.com')              
        self.login.enter_password('Edx123@#')
        self.login.submit_button()
        print(self.driver.title)
        
        time.sleep(5)
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()