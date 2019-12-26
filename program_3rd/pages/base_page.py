from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

class BasePage(object):

    def __init__(self, driver):
        self.driver = driver

    def find_elem(self, css_selector, timeout=20):
        try:
            return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.CSS_SELECTOR, css_selector)))
        except TimeoutException:
            raise TimeoutException(f'{css_selector} not found')

    def wait_for_element_visibility(self, css_selector, timeout=30):
        try:
            return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.CSS_SELECTOR, css_selector)))
        except TimeoutException:
            raise TimeoutException(f'{css_selector} is not visible')
    
    def wait_for_the_elem_text(self, css_selector, target_text, timeout=30):
        try:
            return WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, css_selector), target_text))
        except TimeoutException:
            raise TimeoutException(f'{css_selector} is not visible')