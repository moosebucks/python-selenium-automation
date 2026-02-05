from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page

class SignInPage(Page):

    TERMS_AND_CONDITIONS_LINK =(By.CSS_SELECTOR, "[aria-label*='terms & conditions']")

    def open_sign_in_page(self):
        self.open_url("https://www.target.com/orders?lnk=acct_nav_my_account")

    def click_terms_and_conditions_link(self):
         self.wait_until_clickable_click(*self.TERMS_AND_CONDITIONS_LINK)

    def verify_sign_in_page(self):
        self.verify_url_contains("login")
