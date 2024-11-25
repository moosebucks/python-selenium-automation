from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('Open Target main page')
def open_main(context):
    context.driver.get('https://www.target.com')

@when('Search for tea')
def search_product(context):
    context.driver.find_element(By.ID, 'search').send_keys('tea')
    context.driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
    sleep(5)

@then('Verify search results shown')
def verify_product(context):
    actual_result = 'tea'
    expected_result = context.driver.find_element(By.XPATH, "//div[@data-test='resultsHeading']").text
    assert actual_result in expected_result, f'Expected text {expected_result} not in actual {actual_result}'
    print('Test case passed')
