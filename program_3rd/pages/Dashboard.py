from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .base_page import BasePage
class Dashboard(BasePage):

    def __init__(self, driver):
        self.driver = driver

    def is_browser_on_the_page(self):
        self.wait_for_the_elem_text('.btn-neutral', 'Explore New Courses')
        # WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.toggle-user-dropdown')))
        return True  


