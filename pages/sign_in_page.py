from selenium.webdriver.common.by import By
from time import sleep
from pages.base_page import BasePage

class SignInPage(BasePage):
    sign_into_account_banner=(By.XPATH, "//span[text()='Sign into your Target account']")
    terms_and_conditions_link= (By.CSS_SELECTOR, "a[aria-label='terms & conditions - opens in a new window']")

    def verify_sign_in_page(self):
        expected_text= 'Sign into your Target account'
        self.verify_text(expected_text,*self.sign_into_account_banner)

    def click_terms_and_conditions_link(self):
        self.click(*self.terms_and_conditions_link)