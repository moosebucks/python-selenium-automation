from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


driver = webdriver.Chrome()
driver.maximize_window()

# open the url
driver.get('https://stackoverflow.com/users/signup/')
sleep(20)

driver.find_element(By.XPATH, "//h1[text()='Create your account']")
#
# driver.find_element(By.XPATH, "//a[text()='terms of service']").click()
# sleep(2)