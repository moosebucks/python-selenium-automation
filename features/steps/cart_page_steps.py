from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
CART_ICON=(By.CSS_SELECTOR, "[data-test='@web/CartLink']")


@then('Verify "cart is empty” message is shown')
def verify_cart_empty(context):
    context.app.cart_page.verify_cart_empty()

@then('Verify product in cart')
def verify_cart(context):
    context.app.cart_page.verify_cart()
