from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

SEARCH_FIELD= (By.ID, 'search')
SEARCH_BUTTON= (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
CART_ICON= (By.CSS_SELECTOR,"[data-test='@web/CartLink']")

@given('Open Target main page')
def open_main(context):
    context.driver.get('https://www.target.com')

@when('Search for {product}')
def search_product(context, product):
    context.driver.find_element(*SEARCH_FIELD).send_keys(product)
    context.driver.find_element(*SEARCH_BUTTON).click()
    sleep(5)

@then('Verify atleast 1 header link is shown')
def verify_header(context):
    text=context.driver.find_element(By.CSS_SELECTOR, "[data-test*='@web/GlobalHeader/UtilityHeader/']")
    print('Elements:')
    print(text)

@when('Click on Cart icon')
def click_cart(context):
    context.driver.find_element(*CART_ICON).click()
    sleep(2)

@when('Click on Target Circle header')
def click_on_target_circle(context):
    context.driver.find_element(By.ID, 'utilityNav-circle').click()




