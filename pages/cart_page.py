from selenium.webdriver.common.by import By
from time import sleep


from pages.base_page import BasePage


class CartPage(BasePage):
    EMPTY_CART_BANNER= (By.CSS_SELECTOR, "[class='sc-fe064f5c-0 fJliSz']")

    def verify_cart(self):
        expected_result = 'Your cart is empty'
        actual_result = self.find_element(*self.EMPTY_CART_BANNER).text
        assert expected_result in actual_result, f' {expected_result} not in {actual_result}'