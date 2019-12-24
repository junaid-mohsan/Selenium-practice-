from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage():

    def __init__(self, driver):
        self.driver = driver 
        self.username_id = "#login-email"
        self.password_id = "#login-password"

    def is_browser_on_the_hpage(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#footer-language-button')))
        return True

    def is_browser_on_the_loginpage(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button[type="submit"]')))
        return True

           

    def enter_username(self, username):
        # self.driver.find_element_by_css_selector(self.username_id).clear()
        self.driver.find_element_by_css_selector(self.username_id).send_keys(username)

    def enter_password(self, password):
        # self.driver.find_element_by_css_selector(self.password_id).clear() 
        self.driver.find_element_by_css_selector(self.password_id).send_keys(password)

    def submit_button(self):
        self.driver.find_element_by_css_selector('button[type="submit"]').click()

    def logout(self):
        self.driver.find_element_by_css_selector('.fa-caret-down').click()
        self.driver.find_element_by_link_text('Sign Out').click()