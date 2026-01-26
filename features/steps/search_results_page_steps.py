from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep

ADD_TO_CART_BUTTON=(By.CSS_SELECTOR, "[id*='addToCartButtonOrTextId']")
ADD_TO_CART_BUTTON_SIDE_NAV=(By.CSS_SELECTOR,"[data-test='content-wrapper'] [id*='addToCart']")



@then('Search results for {expected_product} are shown')
def verify_search_results(context, expected_product):
    context.app.search_results_page.verify_search_results(expected_product)

@when("Click on add to cart button")
def add_to_cart(context):
    context.driver.find_element(*ADD_TO_CART_BUTTON).click()
    sleep(2)
    # context.driver.wait.until()

@when('Click on add to cart button from the side navigation')
def click_on_add_cart_side_nav(context):
    context.driver.find_element(*ADD_TO_CART_BUTTON_SIDE_NAV).click()
    context.driver.find_element(By.CSS_SELECTOR, "[aria-label='close").click()
    sleep(4)

