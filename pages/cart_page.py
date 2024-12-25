from selenium.webdriver.common.by import By
from time import sleep


from pages.base_page import BasePage


class CartPage(BasePage):
    EMPTY_CART_BANNER= (By.CSS_SELECTOR, "[class='sc-fe064f5c-0 fJliSz']")
    CART_ITEM_TITLE=(By.CSS_SELECTOR, "[data-test='cartItem-title']")
    def verify_cart_empty(self):
        expected_result = 'Your cart is empty'
        self.verify_text(expected_result, *self.EMPTY_CART_BANNER)

    def open_cart_page(self):
        self.driver.get("https://www.target.com/cart")

    def verify_product_name(self):
        self.verify_partial_text(*self.CART_ITEM_TITLE, 'Tea')
