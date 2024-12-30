from selenium.webdriver.common.by import By
from time import sleep
from pages.base_page import BasePage
from selenium.webdriver.common.action_chains import ActionChains

class SearchResultPage(BasePage):
    SEARCH_RESULT= (By.XPATH, "//div[@data-test='resultsHeading']")
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[id*='addToCartButton']")
    ADD_TO_CART_SIDE_NAV_BTN = (By.CSS_SELECTOR, "[data-test='content-wrapper'] [id*='addToCart']")
    PRODUCT_NAME = (By.CSS_SELECTOR, "[data-test='content-wrapper'] h4")
    FAVORITES_BTN=(By.CSS_SELECTOR, "[data-test='FavoritesButton']")
    FAVORITES_TOOLTIP_TXT = (By.XPATH, "//*[text()='Click to sign in and save']")

    def verify_search_result(self, product):
        self.verify_partial_text(product, *self.SEARCH_RESULT)

    def hover_favorites_icon(self):
        self.hover_element(*self.FAVORITES_BTN)

    def verify_search_url(self, product):
        self.verify_partial_url(product)

    def click_add_to_cart(self):
        self.wait_for_and_click(*self.ADD_TO_CART_BTN)

    def click_add_to_cart_from_side(self):
        self.wait_for_and_click(*self.ADD_TO_CART_SIDE_NAV_BTN)

    def verify_fav_tooltip(self):
        self.wait_for_element_visible(*self.FAVORITES_TOOLTIP_TXT)
