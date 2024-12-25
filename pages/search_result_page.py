from selenium.webdriver.common.by import By
from time import sleep
from pages.base_page import BasePage

class SearchResultPage(BasePage):
    SEARCH_RESULT= (By.XPATH, "//div[@data-test='resultsHeading']")
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[id*='addToCartButton']")
    ADD_TO_CART_SIDE_NAV_BTN = (By.CSS_SELECTOR, "[data-test='content-wrapper'] [id*='addToCart']")
    PRODUCT_NAME = (By.CSS_SELECTOR, "[data-test='content-wrapper'] h4")

    def verify_search_result(self, product):
        self.verify_partial_text(product, *self.SEARCH_RESULT)

    def verify_search_url(self, product):
        self.verify_partial_url(product)

    def click_add_to_cart(self):
        self.wait_for_and_click(*self.ADD_TO_CART_BTN)

    def click_add_to_cart_from_side(self):
        self.wait_for_and_click(*self.ADD_TO_CART_SIDE_NAV_BTN)