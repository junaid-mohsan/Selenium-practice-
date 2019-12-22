from selenium.webdriver.support.ui import Select

class Registrer():

    def __init__(self, driver):
        self.driver = driver

        self.email_id = "#register-email"
        self.name_id = "#register-name"
        self.username_id = "#register-username"
        self.password_id = "#register-password"
        self.countrydropdown_id = "#register-country"

    def regemail(self, email):
        self.driver.find_element_by_css_selector(self.email_id).send_keys(email)

    def regname(self, name):
        self.driver.find_element_by_css_selector(self.name_id).send_keys(name)

    def regusername(self, username):
        self.driver.find_element_by_css_selector(self.username_id).send_keys(username)

    def regpassword(self, password):    
        self.driver.find_element_by_css_selector(self.password_id).send_keys(password)

    def regcountry(self, country):
        Select(self.driver.find_element_by_css_selector(self.countrydropdown_id)).select_by_visible_text(country)

    def submitButton(self):
        self.driver.find_element_by_css_selector('button[type="submit"]').click()
