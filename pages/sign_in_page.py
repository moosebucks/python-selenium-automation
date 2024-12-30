from selenium.webdriver.common.by import By
from time import sleep
from pages.base_page import BasePage

class SignInPage(BasePage):
    sign_into_account_banner=(By.XPATH, "//span[text()='Sign into your Target account']")
    terms_and_conditions_link= (By.CSS_SELECTOR, "a[aria-label='terms & conditions - opens in a new window']")
    SIGN_IN_EMAIL_TAB=(By.ID, 'username')
    SIGN_IN_PASSWORD_TAB=(By.ID, 'password')
    SIGN_IN_WITH_PASSWORD_BTN=(By.ID, 'login')
    WE_CANT_FIND_YOUR_ACCOUNT_TXT= (By.CSS_SELECTOR, "[data-test='authAlertDisplay']")

    def verify_sign_in_page(self):
        expected_text= 'Sign into your Target account'
        self.verify_text(expected_text,*self.sign_into_account_banner)

    def click_terms_and_conditions_link(self):
        self.click(*self.terms_and_conditions_link)

    def enter_incorrect_credentials(self):
        self.input_text('moussadiak3900@gmail.com', *self.SIGN_IN_EMAIL_TAB)
        self.input_text('Password123', *self.SIGN_IN_PASSWORD_TAB)
        sleep(2)

    def click_sign_in_with_password_btn(self):
        self.click(*self.SIGN_IN_WITH_PASSWORD_BTN)

    def verify_we_cant_find_your_account_message_is_shown(self):
        self.find_element(*self.WE_CANT_FIND_YOUR_ACCOUNT_TXT)


