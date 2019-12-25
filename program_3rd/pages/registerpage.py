from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators.locates import Locators

class Registrer():

    def __init__(self, driver):
        self.driver = driver

        
    def is_browser_on_the_hpage(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#footer-language-button')))
        return True

    def is_browser_on_the_regpage(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button[type="submit"]')))
        return True

    def regemail(self, email):
        self.driver.find_element_by_css_selector(Locators.email_id).clear()
        self.driver.find_element_by_css_selector(Locators.email_id).send_keys(email)

    def regname(self, name):
        self.driver.find_element_by_css_selector(Locators.name_id).clear()
        self.driver.find_element_by_css_selector(Locators.name_id).send_keys(name)

    def regusername(self, username):
        self.driver.find_element_by_css_selector(Locators.username_id).clear()
        self.driver.find_element_by_css_selector(Locators.username_id).send_keys(username)

    def regpassword(self, password):    
        self.driver.find_element_by_css_selector(Locators.password_id).clear()
        self.driver.find_element_by_css_selector(Locators.password_id).send_keys(password)

    def regcountry(self, country):
        Select(self.driver.find_element_by_css_selector(Locators.countrydropdown_id)).select_by_visible_text(country)

    def submitButton(self):
        self.driver.find_element_by_css_selector(Locators.register_btn_id).click()

    def logout(self):
        self.driver.find_element_by_css_selector('.fa-caret-down').click()
        self.driver.find_element_by_link_text('Sign Out').click()
