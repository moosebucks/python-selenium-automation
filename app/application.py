from pages.base_page import BasePage
from pages.cart_page import CartPage
from pages.help_page import HelpPage
from pages.privacy_policy_page import PrivacyPolicyPage
from pages.search_result_page import SearchResultPage
from pages.main_page import MainPage
from pages.header import Header
from pages.sign_in_page import SignInPage
from pages.terms_and_conditions_page import TermsAndConditionsPage


class Application:

    def __init__(self, driver):
        self.driver = driver

        self.base_page = BasePage(driver)
        self.search_result_page = SearchResultPage(driver)
        self.main_page = MainPage(driver)
        self.header = Header(driver)
        self.cart_page = CartPage(driver)
        self.sign_in_page = SignInPage(driver)
        self.privacy_policy_page = PrivacyPolicyPage(driver)
        self.terms_and_conditions_page = TermsAndConditionsPage(driver)
        self.help_page = HelpPage(driver)