from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

ADD_TO_CART_BUTTON=(By.CSS_SELECTOR, "[id*='addToCartButton']")
ADD_TO_CART_BUTTON_SIDE_NAV= (By.CSS_SELECTOR, "[data-test='content-wrapper'] [id='addToCart']")
PRODUCT_NAME = (By.CSS_SELECTOR, "[data-test='content-wrapper'] h4")

@then('Verify “Your cart is empty” message is shown')
def verify_cart(context):
    context.app.cart_page.verify_cart()


@when("Click Add to cart button")
def click_add_to_cart(context):
    context.driver.find_element(*ADD_TO_CART_BUTTON).click()


@when("Click Add to cart button from side navigation")
def click_add_to_cart_from_side(context):
    context.driver.find_element(*ADD_TO_CART_BUTTON_SIDE_NAV).click()


@when("Open cart page")
def open_cart_page(context):
    context.driver.get("https://www.target.com/cart")

@then('Verify cart has {amount} items')
def verify_cart_item(context, amount):
    cart_summary= context.driver.find_element(By.XPATH, "//div[./span[contains(text(), 'subtotal')]]")
    assert f'{amount} item' in cart_summary, f' Expected {amount} but got {cart_summary}'

@then('Verify cart has correct product')
def verify_product_name(context):
    actual_name = context.driver.find_element(By.CSS_SELECTOR, "[data-test='cartItem-title']").text
    print(f'Actual product in cart name: {actual_name}')
    print(f'Product name stored earlier: {context.product_name}')
    assert context.product_name in actual_name, f"Expected {context.product_name} but got {actual_name}"
