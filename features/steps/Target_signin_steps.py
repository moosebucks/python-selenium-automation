from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

SIGN_IN_ICON= (By.XPATH, "//a[@data-test='@web/AccountLink']")
SIGN_IN_SIDE_NAV_BUTTON= (By.CSS_SELECTOR,"[data-test='accountNav-signIn']")

@when('Click Sign In')
def click_sign_in(context):
    context.app.header.click_sign_in()
    # context.driver.find_element(*SIGN_IN_ICON).click()
    # sleep(2)

@when('From right side navigation menu, click Sign In')
def click_sign_in_from_nav_bar(context):
    context.app.header.click_sign_in_from_nav_bar()
    sleep(4)

@then('Verify Sign In form opened')
def verify_sign_in_page(context):
    context.app.sign_in_page.verify_sign_in_page()
