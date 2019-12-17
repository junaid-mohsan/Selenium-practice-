from selenium import webdriver
import unittest
import time

class MckLogin(unittest.TestCase): 
    def setUp(self):
        #Initialize webdriver
        self.driver = webdriver.Chrome("C:\Drivers\chromedriver_win32\chromedriver.exe")
        
    def test_login(self):
        #Target website
        self.driver.get("https://mckinsey:academy@qa.mckinsey.edx.org/")
        #To check the title of website
        self.assertIn('Academy', self.driver.title)
        #To hid the right side bar
        self.driver.find_element_by_css_selector('#djHideToolBarButton').click()
        # Find and fill the username field
        self.driver.find_element_by_css_selector('#login_id').send_keys("")
        # Find and click on the login button  
        self.driver.find_element_by_css_selector('button[id="login"]').click()
        time.sleep(3)
        # Find and fill the password field
        self.driver.find_element_by_css_selector('#password').send_keys("")
        time.sleep(3)
        # Find and click on the login button 
        self.driver.find_element_by_css_selector('button[id="login"]').click()
        time.sleep(5)
        # Print the dashboard title s
        print(self.driver.title)
        self.assertIn('Academy', self.driver.title)
        time.sleep(3)
        
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()