from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page

class Header(Page):
    SEARCH_BAR = (By.ID, 'search')
    SEARCH_BUTTON = (By.CSS_SELECTOR, "[data-test='@web/Search/SearchButton']")
    CART_ICON = (By.CSS_SELECTOR, "[data-test='@web/CartLink']")
    ACCOUNT_BUTTON = (By.ID, 'account-sign-in')
    SIDE_NAV_SIGNIN_BUTTON = (By.CSS_SELECTOR, "[data-test='accountNav-signIn']")

    def search(self, product):
        self.input_text(product, *self.SEARCH_BAR)
        sleep(2)
        self.click(*self.SEARCH_BUTTON)
        sleep(10)

    def click_cart_icon(self):
        self.wait_until_clickable_click(*self.CART_ICON)

    def click_account_btn(self):
        self.wait_until_clickable_click(*self.ACCOUNT_BUTTON)

    def click_sign_in_btn(self):
        self.wait_until_clickable_click(*self.SIDE_NAV_SIGNIN_BUTTON)

