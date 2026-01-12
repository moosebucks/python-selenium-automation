from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


driver = webdriver.Chrome()
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_ya_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&')

#Amazon logo
driver.find_element(By.XPATH, "//i[@class='a-icon a-icon-logo']")

#email field
driver.find_element(By.XPATH, "//input[@type='email']")

#continue button
driver.find_element(By.XPATH, "//input[@type='submit']")

#Conditions of Use link
driver.find_element(By.XPATH, "//a[text()='Conditions of Use']")

#Privacy Notice link
driver.find_element(By.XPATH, "//a[text()='Privacy Notice']")

#Need help button
driver.find_element(By.XPATH, "//a[contains(@href,'account-issues')]")
sleep(2)
