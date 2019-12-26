from selenium.webdriver.support.ui import Select
from .base_page import BasePage

class Registrer(BasePage):

    def __init__(self, driver):
        self.driver = driver

        self.email_id = "#register-email"
        self.name_id = "#register-name"
        self.username_id = "#register-username"
        self.password_id = "#register-password"
        self.countrydropdown_id = "#register-country"
        self.submit_btn = "button[type='submit']"

    def is_browser_on_the_hpage(self):
        self.wait_for_element_visibility('#footer-language-button')
        return True

    def is_browser_on_the_regpage(self):
        self.wait_for_element_visibility('button[type="submit"]')
        return True

    def regemail(self, email):
        self.find_elem(self.email_id).clear()
        self.find_elem(self.email_id).send_keys(email)

    def regname(self, name):
        self.find_elem(self.name_id).clear()
        self.find_elem(self.name_id).send_keys(name)

    def regusername(self, username):
        self.find_elem(self.username_id).clear()
        self.find_elem(self.username_id).send_keys(username)

    def regpassword(self, password):    
        self.find_elem(self.password_id).clear()
        self.find_elem(self.password_id).send_keys(password)

    def regcountry(self, country):
        Select(self.find_elem(self.countrydropdown_id)).select_by_visible_text(country)

    def submitButton(self):
        self.find_elem(self.submit_btn).click()

    def logout(self):
        self.find_elem('.fa-caret-down').click()
        self.driver.find_element_by_link_text('Sign Out').click()
