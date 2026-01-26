from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page

class Header(Page):
    SEARCH_BAR = (By.ID, 'search')
    SEARCH_BUTTON = (By.CSS_SELECTOR, "[data-test='@web/Search/SearchButton']")
    CART_ICON = (By.CSS_SELECTOR, "[data-test='@web/CartLink']")

    def search(self, product):
        self.input_text(product, self.SEARCH_BAR)
        sleep(2)
        self.click(*self.SEARCH_BUTTON)
        sleep(10)

    def click_cart_icon(self):
        self.click(*self.CART_ICON)
