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
        self.driver.find_element_by_css_selector('a[id="djHideToolBarButton"]').click()
        # Find and fill the username field
        self.driver.find_element_by_css_selector('#login_id').send_keys("junaid")
        # Find and click on the login button  
        self.driver.find_element_by_css_selector('button[id="login"]').click()
        time.sleep(3)
        # Find and fill the password field
        self.driver.find_element_by_css_selector('#password').send_keys("ARbi12.,")
        time.sleep(3)
        # Find and click on the login button 
        self.driver.find_element_by_css_selector('button[id="login"]').click()
        time.sleep(5)
        # Print the dashboard title 
        print(self.driver.title)
        # Find and Click on the admin link
        self.driver.find_element_by_xpath('/html/body/header/div/div/div/div/div[2]/nav/ul/li[2]/a').click()
        time.sleep(5)
        # Find and Click on the course link
        self.driver.find_element_by_xpath('//*[@id="admin-body"]/header/div[1]/div/nav/ul/li[1]/a').click()
        time.sleep(3)
        # Find and write on the search bar to find the results
        self.driver.find_element_by_css_selector('input[name="search"]').send_keys("test/01/2019")
        time.sleep(3)
        
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()