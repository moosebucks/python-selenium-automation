from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@when('Click on Cart icon')
def click_cart(context):
    context.driver.find_element(By.CSS_SELECTOR,"[data-test='@web/CartLink']").click()
    sleep(2)

@then('Verify “Your cart is empty” message is shown')
def verify_cart(context):
    actual_result='Your cart is empty'
    expected_result=context.driver.find_element(By.XPATH,"//h1[@class='sc-fe064f5c-0 dtCtuk']").text
    assert actual_result in expected_result