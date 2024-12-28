from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

SEARCH_FIELD= (By.ID, 'search')
SEARCH_BUTTON= (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
CART_ICON= (By.CSS_SELECTOR,"[data-test='@web/CartLink']")

@given('Open Target main page')
def open_main(context):
    context.app.main_page.open_main()

@when('Search for {product}')
def search_product(context, product):
    context.app.header.search_product(product)


@then('Verify atleast 1 header link is shown')
def verify_header(context):
    text=context.driver.find_element(By.CSS_SELECTOR, "[data-test*='@web/GlobalHeader/UtilityHeader/']")
    print('Elements:')
    print(text)

@when('Click on Cart icon')
def click_cart(context):
    context.app.header.click_cart()

@when('Click on Target Circle header')
def click_on_target_circle(context):
    context.driver.find_element(By.ID, 'utilityNav-circle').click()


#Target circle page
@then('Verify atleast {Expected_result} benefit cells are shown')
def verify_result(context, Expected_result):
    cells=context.driver.find_elements(By.CSS_SELECTOR, ".cell-item-content")
    print("Beneift Cells:")
    print(len(cells))
    assert len(cells) >= int(Expected_result), f'{len(cells)} cells did not match the right amount'

