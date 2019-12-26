from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .base_page import BasePage

class LoginPage(BasePage):

    def __init__(self, driver):
        self.driver = driver 
        self.username_id = "#login-email"
        self.password_id = "#login-password"
        self.login_btn = "button[type='submit']"
        

    def is_browser_on_the_hpage(self):
        self.wait_for_element_visibility('#footer-language-button')
        # WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#footer-language-button')))
        return True

    def is_browser_on_the_loginpage(self):  
        self.wait_for_element_visibility('button[type="submit"]')      
        # WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button[type="submit"]')))
        return True

    def enter_username(self, username):
        # self.driver.find_element_by_css_selector(self.username_id).clear()
        self.find_elem(self.username_id).send_keys(username)
        # self.driver.find_element_by_css_selector(self.username_id).send_keys(username)

    def enter_password(self, password):
        # self.driver.find_element_by_css_selector(self.password_id).clear() 
        self.find_elem(self.password_id).send_keys(password)
        # self.driver.find_element_by_css_selector(self.password_id).send_keys(password)

    def submit_button(self):
        self.find_elem(self.login_btn).click()
        # self.driver.find_element_by_css_selector(self.login_btn).click()

    def logout(self):
        self.find_elem('.fa-caret-down').click()
        self.driver.find_element_by_link_text('Sign Out').click()
        