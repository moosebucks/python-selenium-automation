from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open Help page for Returns')
def click_cart(context):
    context.app.help_page.open_help_returns()
    sleep(4)


@when('Select Help topic {dd_option_value}')
def select_promotions(context, dd_option_value):
    context.app.help_page.select_promotions(dd_option_value)


# @then('Verify help Returns page opened')
# def verify_returns_opened(context):
#     context.app.help_page.verify_returns_opened()
#
#
# @then('Verify help Current promotions page opened')
# def verify_promotions_opened(context):
#     context.app.help_page.verify_promotions_opened()


@then('Verify help {selected_header} page opened')
def verify_help_page_topic_opened(context, selected_header):
    context.app.help_page.verify_help_page_topic_opened(selected_header)