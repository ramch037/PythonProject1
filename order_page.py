from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class OrderPage:
    def __init__(self, driver):
        self.driver = driver
        self.country_dropdown = (By.XPATH, '//select')
        self.checkbox_terms_conditions = (By.XPATH, '//input[@type="checkbox"]')
        self.proceed_button = (By.XPATH, '//button[text()="Proceed"]')


    def select_country(self, country):
        country_dropdown = Select(self.driver.find_element(*self.country_dropdown))
        country_dropdown.select_by_visible_text(country)

    def select_checkbox_terms_conditions(self):
        self.driver.find_element(*self.checkbox_terms_conditions).click()

    def click_proceed_button(self):
        self.driver.find_element(*self.proceed_button).click()


