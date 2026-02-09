from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page

class SignInPage(Page):

    TERMS_AND_CONDITIONS_LINK =(By.CSS_SELECTOR, "[aria-label*='terms & conditions']")
    EMAIL_TAB=(By.CSS_SELECTOR, "[id='username']")
    CONTINUE_BTN=(By.CSS_SELECTOR, "[id='login']")
    ENTER_YOUR_PASSWORD_BTN = (By.CSS_SELECTOR, "[id='password']")
    PASSWORD_BAR = (By.CSS_SELECTOR, "[data-test='login-password']")
    SIGN_IN_WITH_PASSWORD_BTN = (By.CSS_SELECTOR, "[type='submit']")
    LOCKED_ACCOUNT_MSG = (By.XPATH, "//*[contains(text(),'Forgot Password')]")

    def open_sign_in_page(self):
        self.open_url("https://www.target.com/orders?lnk=acct_nav_my_account")

    def click_terms_and_conditions_link(self):
         self.wait_until_clickable_click(*self.TERMS_AND_CONDITIONS_LINK)

    def verify_sign_in_page(self):
        self.verify_url_contains("login")

    def enter_correct_email_and_click_continue(self):
        self.input_text('moussadiak300@gmail.com',*self.EMAIL_TAB )
        self.wait_until_clickable_click(*self.CONTINUE_BTN)

    def enter_incorrect_password(self):
        self.wait_until_clickable_click(*self.ENTER_YOUR_PASSWORD_BTN)
        self.input_text('MO123443', *self.PASSWORD_BAR)

    def click_sign_in_with_password(self):
        self.wait_until_clickable_click(*self.SIGN_IN_WITH_PASSWORD_BTN)
        sleep(3)

    def verify_error_message_shown(self):
        text=self.find_element(*self.LOCKED_ACCOUNT_MSG).text
        print(text)



