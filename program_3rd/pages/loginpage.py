# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

from locators.locates import Locators
from .basepage import Basepage

class LoginPage(Basepage):

    def __init__(self, driver):
        self.driver = driver 

    def is_browser_on_the_hpage(self):
        self.wait_for_the_element('#footer-language-button')
        # WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#footer-language-button')))
        return True

    def is_browser_on_the_loginpage(self):
        self.wait_for_the_element('button[type="submit"]')
        # WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button[type="submit"]')))
        return True

           
    def enter_username(self, username):        
        # self.find_elem(Locators.username_id).clear()
        print(Locators.username_id)
        # self.find_elem(Locators.username_id).send_keys(username)

        # self.driver.find_element_by_css_selector(self.username_id).clear()
        # self.driver.find_element_by_css_selector(Locators.username_id).send_keys(username)

    def enter_password(self, password):
        # self.find_elem(Locators.password_id).clear()
        print(Locators.password_id)
        # self.find_elem(Locators.password_id).send_keys(password)

        # self.driver.find_element_by_css_selector(self.password_id).clear() 
        # self.driver.find_element_by_css_selector(Locators.password_id).send_keys(password)

    def submit_button(self):
        self.find_elem(Locators.login_btn_id).click()
        # self.driver.find_element_by_css_selector(Locators.login_btn_id).click()

    def logout(self):
        self.find_elem(Locators.dropdown_id).click()
        self.find_elem(Locators.select_signout_link).click()

        # self.driver.find_element_by_css_selector(Locators.dropdown_id).click()
        # self.driver.find_element_by_link_text(Locators.select_signout_link).click()