import time

import pytest
from selenium import webdriver



@pytest.fixture()
def test_browser_setup_teardown():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
    driver.implicitly_wait(5)
    yield driver
    driver.quit()
