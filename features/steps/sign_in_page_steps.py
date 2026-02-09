from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep



@given('Open Target sign in page')
def open_sign_in_page(context):
    context.app.sign_in_page.open_sign_in_page()
    sleep(3)

@when('Enter correct email and click Continue')
def enter_correct_email_and_click_continue(context):
    context.app.sign_in_page.enter_correct_email_and_click_continue()

@when('Enter incorrect password')
def enter_incorrect_password(context):
    context.app.sign_in_page.enter_incorrect_password()

@when('Click Sign in with password')
def click_sign_in(context):
    context.app.sign_in_page.click_sign_in_with_password()

@then('Verify Sign In page')
def verify_sign_in_page(context):
    context.app.sign_in_page.verify_sign_in_page()

@then('Verify that an error message is shown')
def verify_sign_in_error_message(context):
    context.app.sign_in_page.verify_error_message_shown()

