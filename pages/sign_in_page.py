from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page

class SignInPage(Page):


    def verify_sign_in_page(self):
        self.verify_url_contains("login")
