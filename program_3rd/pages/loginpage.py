from .base_page import BasePage

class LoginPage(BasePage):

    def __init__(self, driver):
        self.driver = driver 
        self.username_id = "#login-email"
        self.password_id = "#login-password"
        self.login_btn = "button[type='submit']"
        

    def is_browser_on_the_hpage(self):
        self.wait_for_element_visibility('#footer-language-button')
        return True

    def is_browser_on_the_loginpage(self):  
        self.wait_for_element_visibility('button[type="submit"]')      
        return True

    def enter_username(self, username):
        self.find_elem(self.username_id).clear()
        self.find_elem(self.username_id).send_keys(username)

    def enter_password(self, password):
        self.find_elem(self.password_id).clear()
        self.find_elem(self.password_id).send_keys(password)

    def submit_button(self):
        self.find_elem(self.login_btn).click()

    def logout(self):
        self.find_elem('.fa-caret-down').click()
        self.driver.find_element_by_link_text('Sign Out').click()
        