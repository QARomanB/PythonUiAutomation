from selenium.webdriver.common.by import By


class ProductPage:

    def __init__(self, driver):
        self.driver = driver

    def check_that_the_title_is_correct(self, title):
        actual_title_element = self.driver.find_element(By.CSS_SELECTOR, 'h2')
        assert actual_title_element.text == title
