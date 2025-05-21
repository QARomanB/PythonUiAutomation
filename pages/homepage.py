from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get('https://demoblaze.com/')

    def click_galaxy_s6(self):
        wait = WebDriverWait(self.driver, 10)
        galaxy_s6 = wait.until(EC.presence_of_element_located((By.XPATH, '//a[text() = "Samsung galaxy s6"]')))
        galaxy_s6.click()

    def click_monitor_link(self):
        # wait = WebDriverWait(self.driver, 10)
        monitor_link = self.driver.find_element(By.CSS_SELECTOR, '''[onclick="byCat('monitor')"]''')
        monitor_link.click()
        time.sleep(3)

    def check_products_count(self, count):
        monitors = self.driver.find_elements(By.CSS_SELECTOR, ' .card')
        assert len(monitors) == count
