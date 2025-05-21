import time
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
from pages.homepage import HomePage
from pages.product import ProductPage


def test_open_s6_page(driver):

    homepage = HomePage(driver)
    homepage.open()
    homepage.click_galaxy_s6()
    productpage = ProductPage(driver)
    productpage.check_that_the_title_is_correct('Samsung galaxy s6')
    # driver.get('https://demoblaze.com/')
    # wait = WebDriverWait(driver, 10)
    # galaxy_s6 = wait.until(EC.presence_of_element_located((By.XPATH, '//a[text() = "Samsung galaxy s6"]')))
    # galaxy_s6.click()
    # driver.implicitly_wait(3)
    # title = driver.find_element(By.CSS_SELECTOR, 'h2')
    # assert title.text == 'Samsung galaxy s6'


def test_tool_monitors(driver):
    homepage = HomePage(driver)
    homepage.open()
    homepage.click_monitor_link()
    # driver.get('https://demoblaze.com/')
    # wait = WebDriverWait(driver, 10)
    # monitor_link = driver.find_element(By.CSS_SELECTOR, '''[onclick="byCat('monitor')"]''')
    # monitor_link.click()
    time.sleep(3)
    # monitors = driver.find_elements(By.CSS_SELECTOR, ' .card')
    # assert len(monitors) == 2
    homepage.check_products_count(2)

# def test_tool_monitors(driver):
#     driver.get('https://demoblaze.com/')
#     wait = WebDriverWait(driver, 10)
#
#     # Click the "Monitors" category
#     monitor_link = wait.until(EC.element_to_be_clickable(
#         (By.CSS_SELECTOR, '[onclick="byCat(\'monitor\')"]')))
#     monitor_link.click()
#
#     # Wait for a known monitor product to load
#     wait.until(EC.presence_of_element_located(
#         (By.XPATH, "//a[text()='Apple monitor 24']")))
#
#     # Get product titles
#     titles_elements = driver.find_elements(By.CSS_SELECTOR, 'a.hrefch')
#     titles = [elem.text for elem in titles_elements]
#     print("Monitor Titles:", titles)
#
#     # Validate the expected monitors are shown
#     assert "Apple monitor 24" in titles
#     assert "ASUS Full HD" in titles
#     assert len(titles) == 2
