from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

from pages.base_page import Page



class SearchResultsPage(Page):
    SEARCH_RESULTS_TEXT = (By.XPATH, "//div[contains(@class,'styles_listingPageResultsCount')]")
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "[id*='addToCartButtonOrTextId']")
    ADD_TO_CART_BUTTON_SIDE_NAV = (By.CSS_SELECTOR, "[data-test='content-wrapper'] [id*='addToCart']")

    def verify_search_results(self, expected_product):
        self.verify_partial_text(expected_product, *self.SEARCH_RESULTS_TEXT)

    def click_add_to_cart_btn(self):
        self.wait_until_clickable_click(*self.ADD_TO_CART_BUTTON)
        sleep(4)

    def click_on_add_cart_side_nav(self):
        self.wait_until_clickable_click(*self.ADD_TO_CART_BUTTON_SIDE_NAV)
        self.wait_until_clickable_click(By.CSS_SELECTOR, "[aria-label='close']")

