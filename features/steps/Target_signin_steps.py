from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

SIGN_IN_ICON= (By.XPATH, "//a[@data-test='@web/AccountLink']")
SIGN_IN_SIDE_NAV_BUTTON= (By.CSS_SELECTOR,"[data-test='accountNav-signIn']")
@when('Click Sign In')
def click_sign_in(context):
    context.driver.find_element(*SIGN_IN_ICON).click()
    sleep(2)

@when('From right side navigation menu, click Sign In')
def click_from_nav_bar(context):
    context.driver.find_element(*SIGN_IN_SIDE_NAV_BUTTON).click()

@then('Verify Sign In form opened')
def verify_sign_in(context):
    actual_result= 'Sign into your Target account'
    expected_result =context.driver.find_element(By.XPATH,"//span[text()='Sign into your Target account']").text
    assert actual_result in expected_result
