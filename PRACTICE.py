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

# driver.get('https://www.google.com/')
# sleep(3)
#
# driver.find_element(By.ID, 'APjFqb').send_keys('Ebay')
# sleep(2)
# driver.find_element(By.XPATH, "//div[@class='sbic vYOkbe']").click()
# driver.find_element(By.XPATH, "//h3[@class='LC20lb MBeuO DKV0Md']").click()
# driver.find_element(By.ID, 'gh-ac').send_keys('Cars')
# driver.find_element(By.ID, 'gh-btn').click()
#
# sleep(3)
#
# expected_result='Find a car or truck'
# actual_result=driver.find_element(By.ID, 'uf-template-vehicle-finder-ct-title').text
# print(actual_result)

driver.find_element(By.CSS_SELECTOR, '#twotabsearchtextbox')
driver.find_element(By.CSS_SELECTOR, '.nav-input.nav-progressive-attribute)
