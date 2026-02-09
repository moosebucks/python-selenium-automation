from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep

ADD_TO_CART_BUTTON=(By.CSS_SELECTOR, "[id*='addToCartButtonOrTextId']")
ADD_TO_CART_BUTTON_SIDE_NAV=(By.CSS_SELECTOR,"[data-test='content-wrapper'] [id*='addToCart']")



@when('Hover favorites icon')
def hover_fav_icon(context):
    context.app.search_results_page.hover_fav_icon()

@then('Search results for {expected_product} are shown')
def verify_search_results(context, expected_product):
    context.app.search_results_page.verify_search_results(expected_product)

@when("Click on add to cart button")
def add_to_cart(context):
    context.app.search_results_page.click_add_to_cart_btn()
    # context.driver.wait.until()

@when('Click on add to cart button from the side navigation')
def click_on_add_cart_side_nav(context):
    context.app.search_results_page.click_on_add_cart_side_nav()

@then('Favorites tooltip is shown')
def verify_fav_tooltip(context):
    context.app.search_results_page.verify_fav_tooltip()
