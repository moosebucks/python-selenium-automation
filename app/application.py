from pages.base_page import BasePage
from pages.cart_page import CartPage
from pages.search_result_page import SearchResultPage
from pages.main_page import MainPage
from pages.header import Header

class Application:

    def __init__(self, driver):
        self.driver = driver

        self.base_page = BasePage(driver)
        self.search_result_page = SearchResultPage(driver)
        self.main_page = MainPage(driver)
        self.header = Header(driver)
        self.cart_page = CartPage(driver)

