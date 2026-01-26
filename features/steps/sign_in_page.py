from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@then('Verify Sign In page')
def verify_sign_in_page(context):
    expected_text = "Sign in or create account"
    actual_text = context.driver.find_element(By.XPATH, "//h1[text()='Sign in or create account']").text
    print(actual_text)
    assert expected_text in actual_text, f'Expected text {expected_text} not in actual text {actual_text}'
