from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep




@then('Verify search results shown for {product}')
def verify_search_result(context, product):
    context.app.search_result_page.verify_search_result(product)

@then('Verify search term {product} in URL')
def verify_search_url(context, product):
    context.app.search_result_page.verify_search_url(product)

@when('Stored product name')
def stored_product_name(context):
    context.product_name = context.driver.find_element(*PRODUCT_NAME).text
    print(f'Product stored: {context.product_name}')

@when('Hover favorites icon')
def hover_favorites_icon(context):
    context.app.search_result_page.hover_favorites_icon()

@then('Verify Favorites tooltip is shown')
def favorites_tootltip(context):
    context.app.search_result_page.verify_fav_tooltip()

