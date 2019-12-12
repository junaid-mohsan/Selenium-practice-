from selenium import webdriver
import unittest
import time

class EdxLogin(unittest.TestCase): 
    def setUp(self):
        self.driver = webdriver.Chrome("C:\Drivers\chromedriver_win32\chromedriver.exe")
        
    def test_login(self):
        self.driver.get("https://mckinsey:academy@qa.mckinsey.edx.org/")
        self.driver.find_element_by_css_selector('a[id="djHideToolBarButton"]').click()

        self.driver.find_element_by_css_selector('#login_id').send_keys("")

        self.driver.find_element_by_css_selector('button[id="login"]').click()
        time.sleep(3)

        self.driver.find_element_by_css_selector('#password').send_keys("")
        self.driver.find_element_by_css_selector('button[id="login"]').click()
        time.sleep(3)

        self.driver.find_element_by_xpath('/html/body/header/div/div/div/div/div[2]/nav/ul/li[2]/a').click()
        time.sleep(5)
        self.driver.find_element_by_xpath('//*[@id="admin-body"]/header/div[1]/div/nav/ul/li[1]/a').click()
        time.sleep(3)

        self.driver.find_element_by_css_selector('input[name="search"]').send_keys("test/01/2019")

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()