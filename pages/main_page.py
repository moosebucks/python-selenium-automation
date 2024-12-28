from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from time import sleep


class MainPage(BasePage):
    PRIVACY_POLICY_LINK = (By.XPATH, "//a[text()='Privacy policy']")
    SIGN_IN_ICON = (By.XPATH, "//a[@data-test='@web/AccountLink']")
    SIGN_IN_SIDE_NAV_BUTTON = (By.CSS_SELECTOR, "[data-test='accountNav-signIn']")

    def open_main(self):
        self.open_url('https://www.target.com')

    def click_privacy_policy(self):
        self.click(*self.PRIVACY_POLICY_LINK)

    def open_sign_in_page(self):
        self.open_url('https://www.target.com/login')
        self.click(*self.SIGN_IN_ICON)
        self.click(*self.SIGN_IN_SIDE_NAV_BUTTON)
        sleep(3)

