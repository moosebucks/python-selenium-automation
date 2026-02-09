from time import sleep

from behave import given, when, then


@given('Open Target App page')
def open_target_app_page(context):
    context.app.target_app_page.open_target_app()

@when('Click on Terms and Conditions link')
def click_terms_and_conditions_link(context):
    context.app.sign_in_page.click_terms_and_conditions_link()
    sleep(3)

@when('Click Privacy Policy link')
def click_pp_link(context):
    context.app.target_app_page.click_pp_link()

