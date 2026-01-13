from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open Target main page')
def open_main(context):
    context.driver.get('https://www.target.com/')


@when('Search for tea')
def search_product(context):
    context.driver.find_element(By.ID, 'search').send_keys('tea')
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/Search/SearchButton']").click()


@then('Search results for tea are shown')
def verify_search_results(context):
    expected_text = 'tea'
    actual_text = context.driver.find_element(By.XPATH, "//div[contains(@class,'styles_listingPageResultsCount')]").text
    print(actual_text)
    assert expected_text in actual_text, f'Expected text {expected_text} not in actual text {actual_text}'


@when('Click on cart icon')
def click_cart_icon(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/CartLink']").click()

@then('Verify "cart is empty” message is shown')
def verify_cart_empty(context):
    expected_text = 'Your cart is empty'
    actual_text=context.driver.find_element(By.XPATH, "//h1[text()='Your cart is empty']").text
    print(actual_text)
    assert expected_text in actual_text, f'Expected text {expected_text} not in actual text {actual_text}'

@when('Click on account button')
def click_account_button(context):
    context.driver.find_element(By.ID, 'account-sign-in').click()

@when('Click Sign In button')
def click_sign_in_button(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='accountNav-signIn']").click()

@then('Verify Sign In page')
def verify_sign_in_page(context):
    expected_text = "Sign in or create account"
    actual_text = context.driver.find_element(By.XPATH, "//h1[text()='Sign in or create account']").text
    print(actual_text)
    assert expected_text in actual_text, f'Expected text {expected_text} not in actual text {actual_text}'

