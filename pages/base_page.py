from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open_url(self, url):
        self.driver.get(url)

    def get_url(self):
        return self.driver.current_url

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)

    def click(self, *locator):
        self.driver.find_element(*locator).click()

    def input_text(self, text, *locator):
        self.driver.find_element(*locator).send_keys(text)

    def wait_for_element_visible(self, *locator):
        return self.wait.until(
            EC.visibility_of_element_located(locator),
            message= f'Element by {locator} not visible')

    def wait_for_element_invisible(self, *locator):
        self.wait.until(
            EC.invisibility_of_element_located(locator),
            message= f'Element by {locator} should not visible')

    def wait_for_element_clcikable(self, *locator):
        return self.wait.until(
            EC.element_to_be_clickable(locator),
            message=f'Element by {locator} not clcickable')

    def wait_for_and_click(self, *locator):
        self.wait.until(
            EC.element_to_be_clickable(locator),
            message= f'Element by {locator} not clcickable').click()


    def verify_partial_text(self, expected_text, *locator):
        actual_text = self.find_element(*locator).text
        assert expected_text in actual_text, f' {expected_text} not in {actual_text}'

    def verify_text(self, expected_text, *locator):
        actual_text= self.find_element(*locator).text
        assert expected_text == actual_text, f' {expected_text} not in {actual_text}'

    def verify_partial_url(self, expected_url):
        actual_url=self.driver.current_url
        assert expected_url in actual_url, f' {expected_url} does not match {actual_url}'