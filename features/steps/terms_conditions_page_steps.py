from time import sleep

from behave import given, when, then



@then('Verify Terms and Conditions page is opened')
def verify_terms_conditions_page(context):
    context.app.terms_conditions_page.verify_terms_conditions_page()
