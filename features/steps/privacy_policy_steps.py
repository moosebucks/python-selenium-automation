from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep

@when('Click Privacy Policy link')
def click_privacy_policy(context):
    context.app.main_page.click_privacy_policy()

@then('Verify Privacy Policy page opened')
def verify_privacy_policy_opened(context):
    context.app.privacy_policy_page.verify_privacy_policy_opened()

@then('Close current page')
def close_current_page(context):
    context.app.base_page.close_current_page()
    sleep(2)

@then('Return to original window')
def return_to_original_window(context):
    context.app.base_page.switch_to_window_by_id(context.original_window)