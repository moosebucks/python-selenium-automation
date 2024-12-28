from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep

@given('Store original window')
def store_original_window(context):
    context.original_window = context.app.base_page.get_current_window_handle()


@when('Switch to new window')
def switch_to_new_window(context):
    context.app.base_page.switch_to_new_window()
    sleep(3)
    # print('All Windows', context.driver.window_handles)
    # context.driver.switch_to.window(context.driver.window_handles[1])