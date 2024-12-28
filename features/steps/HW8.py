from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('Open sign in page')
def open_sign_in_page(context):
    context.app.main_page.open_sign_in_page()

@when('Store original window')
def store_original_window(context):
    context.original_window=context.app.base_page.get_current_window_handle()
    sleep(4)

@when('Click on Target terms and conditions link')
def click_terms_and_conditions_link(context):
    context.app.sign_in_page.click_terms_and_conditions_link()
    sleep(2)

@when('Switch to the newly opened window')
def switch_to_new_window(context):
    context.app.base_page.switch_to_new_window()
    sleep(2)

@then('Verify Terms and Conditions page is opened')
def verify_terms_and_conditions_page(context):
    context.app.terms_and_conditions_page.verify_terms_and_conditions_page()
    sleep(2)

@then('User can close new window and switch back to original')
def switch_to_original_window(context):
    context.app.base_page.close_current_page()
    sleep(2)
    context.app.base_page.switch_to_window_by_id(context.original_window)
    sleep(2)

