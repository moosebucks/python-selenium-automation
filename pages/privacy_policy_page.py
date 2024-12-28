from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class PrivacyPolicyPage(BasePage):

    def verify_privacy_policy_opened(self):
        self.verify_partial_url('target-privacy-policy')