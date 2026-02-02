from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page

class CartPage(Page):
 EMPTY_CART_MSG=(By.XPATH, "//h1[text()='Your cart is empty']")

 def verify_cart_empty(self):
    self.verify_partial_text('Your cart is empty', *self.EMPTY_CART_MSG)

 def verify_cart(self):
     self.find_element(By.XPATH, "//span[text()='1 item']")