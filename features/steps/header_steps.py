from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
SEARCH_BAR=(By.ID, 'search')
SEARCH_BUTTON=(By.CSS_SELECTOR, "[data-test='@web/Search/SearchButton']")
CART_ICON=(By.CSS_SELECTOR, "[data-test='@web/CartLink']")
ACCOUNT_BUTTON=(By.ID, 'account-sign-in')
SIGNIN_BUTTON=(By.CSS_SELECTOR, "[data-test='accountNav-signIn']")


@when('Search for {product}')
def search_product(context, product):
    context.app.header.search(product)

@when('Click on cart icon')
def click_cart_icon(context):
    context.app.header.click_cart_icon()

@when('Click on account button')
def click_account_button(context):
    context.app.header.click_account_btn()

@when('From right side navigation menu, click Sign In')
def click_sign_in_button(context):
    context.app.header.click_sign_in_btn()