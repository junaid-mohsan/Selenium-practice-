from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .base_page import BasePage
class Registrer(BasePage):

    def __init__(self, driver):
        self.driver = driver

        self.email_id = "#register-email"
        self.name_id = "#register-name"
        self.username_id = "#register-username"
        self.password_id = "#register-password"
        self.countrydropdown_id = "#register-country"

    def is_browser_on_the_hpage(self):
        self.wait_for_element_visibility('#footer-language-button')
        # WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#footer-language-button')))
        return True

    def is_browser_on_the_regpage(self):
        self.wait_for_element_visibility('button[type="submit"]')
        # WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button[type="submit"]')))
        return True

    def regemail(self, email):
        self.driver.find_element_by_css_selector(self.email_id).clear()
        self.driver.find_element_by_css_selector(self.email_id).send_keys(email)

    def regname(self, name):
        self.driver.find_element_by_css_selector(self.name_id).clear()
        self.driver.find_element_by_css_selector(self.name_id).send_keys(name)

    def regusername(self, username):
        self.driver.find_element_by_css_selector(self.username_id).clear()
        self.driver.find_element_by_css_selector(self.username_id).send_keys(username)

    def regpassword(self, password):    
        self.driver.find_element_by_css_selector(self.password_id).clear()
        self.driver.find_element_by_css_selector(self.password_id).send_keys(password)

    def regcountry(self, country):
        Select(self.driver.find_element_by_css_selector(self.countrydropdown_id)).select_by_visible_text(country)

    def submitButton(self):
        self.driver.find_element_by_css_selector('button[type="submit"]').click()

    def logout(self):
        self.driver.find_element_by_css_selector('.fa-caret-down').click()
        self.driver.find_element_by_link_text('Sign Out').click()
