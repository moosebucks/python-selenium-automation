from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep



@when('Click on Target Circle header')
def click_on_target_circle(context):
    context.driver.find_element(By.ID, 'utilityNav-circle').click()

@then('Verify atleast {Expected_result} benefit cells are shown')
def verify_result(context, Expected_result):
    cells=context.driver.find_elements(By.CSS_SELECTOR, ".cell-item-content")
    print("Beneift Cells:")
    print(len(cells))
    assert len(cells) >= int(Expected_result), f'{len(cells)} cells did not match the right amount'


@when("Click Add to cart button")
def click_add_to_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, "[id*='addToCartButton']").click()


@when('Stored product name')
def stored_product_name(context):
    context.product_name = context.driver.find_element(*PRODUCT_NAME).text
    print(f'Product stored: {context.product_name}')


@when("Click Add to cart button from side navigation")
def click_add_to_cart_from_side(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='content-wrapper'] [id='addToCart']").click()

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

