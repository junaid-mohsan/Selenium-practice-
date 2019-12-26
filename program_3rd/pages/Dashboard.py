
from .base_page import BasePage
class Dashboard(BasePage):

    def __init__(self, driver):
        self.driver = driver

    def is_browser_on_the_page(self):
        self.wait_for_the_elem_text('.btn-neutral', 'Explore New Courses')
        return True  


