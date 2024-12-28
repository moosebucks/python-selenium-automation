from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class TermsAndConditionsPage(BasePage):

    def verify_terms_and_conditions_page(self):
        self.verify_partial_url('terms-conditions')

