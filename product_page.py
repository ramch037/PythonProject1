from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class ProductPage:
    def __init__(self, driver):
        self.driver = driver
        self.search_bar = (By.CSS_SELECTOR, 'input[placeholder="Search for Vegetables and Fruits"]')
        self.add_to_cart = (By.CSS_SELECTOR, 'input[type="submit"]')
        self.product_elements = (By.XPATH, '//div[@class="product"]/div[@class="product-action"]/button')
        self.cart_button = (By.CSS_SELECTOR, '.cart-icon img')
        self.click_proceed_to_checkout_button = (By.XPATH,'//button[text()="PROCEED TO CHECKOUT"]')


    def search_product(self):
        self.driver.find_element(*self.search_bar).send_keys("gr")

    def add_items(self):
        products = self.driver.find_elements(*self.product_elements)
        for product in products:
            product.click()

    def click_cart_button(self):
        self.driver.find_element(*self.cart_button).click()
        print('---')

    def click_proceed_to_checkout(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located(self.click_proceed_to_checkout_button)).click()