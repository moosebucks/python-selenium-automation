from selenium.webdriver.common.by import By

from pages.base_page import Page

class TermsConditionsPage(Page):

    def verify_terms_conditions_page(self):
        self.verify_url_contains('terms-conditions')