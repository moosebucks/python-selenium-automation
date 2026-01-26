from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page

class CartPage(Page):

 def verify_cart_page(self):
    expected_text = 'Your cart is empty'
    actual_text = self.driver.find_element(By.XPATH, "//h1[text()='Your cart is empty']").text
    print(actual_text)
    assert expected_text in actual_text, f'Expected text {expected_text} not in actual text {actual_text}'

