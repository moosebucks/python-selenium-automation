from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep




@then('Verify search results shown for {product}')
def verify_search_result(context, product):
    context.app.search_result_page.verify_search_result(product)

@when('Stored product name')
def stored_product_name(context):
    context.product_name = context.driver.find_element(*PRODUCT_NAME).text
    print(f'Product stored: {context.product_name}')
