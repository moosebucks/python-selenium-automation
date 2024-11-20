from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

driver.get('https://www.target.com/')
sleep(5)

driver.find_element(By.XPATH, "//a[@data-test='@web/AccountLink']").click()
sleep(2)
driver.find_element(By.XPATH, "//button[@data-test='accountNav-signIn']").click()
sleep(3)

expected_result='Sign into your Target account'
actual_result=driver.find_element(By.XPATH, "//span[text()='Sign into your Target account']").text
print(actual_result)
sleep(4)
print()
