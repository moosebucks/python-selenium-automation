from selenium.webdriver.common.by import By
from time import sleep
from pages.base_page import BasePage

class SignInPage(BasePage):
    sign_into_account_banner=(By.XPATH, "//span[text()='Sign into your Target account']")

    def verify_sign_in_page(self):
        expected_text= 'Sign into your Target account'
        self.verify_text(expected_text,*self.sign_into_account_banner)