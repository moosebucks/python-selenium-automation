from selenium.webdriver.common.by import By
from time import sleep


from pages.base_page import BasePage


class Header(BasePage):
    SEARCH_FIELD = (By.ID, 'search')
    SEARCH_BUTTON = (By.CSS_SELECTOR, "[data-test='@web/Search/SearchButton']")
    CART_ICON = (By.CSS_SELECTOR, "[data-test='@web/CartLink']")

    def search_product(self, product):
        self.input_text(product, *self.SEARCH_FIELD)
        self.click(*self.SEARCH_BUTTON)
        sleep(8)

    def click_cart(self):
        self.click(*self.CART_ICON)