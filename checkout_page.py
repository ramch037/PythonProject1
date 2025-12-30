from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.promo_code_box = (By.XPATH,'//input[@placeholder="Enter promo code"]')
        self.promo_code_apply = (By.XPATH,'//button[@class="promoBtn"]')
        self.promo_code_applied_text = (By.XPATH,'//span[@class="promoInfo"]')
        self.place_order_button = (By.XPATH,'//button[text()="Place Order"]')

    def enter_promo_code_apply(self, promocode):
        self.driver.find_element(*self.promo_code_box).clear()
        self.driver.find_element(*self.promo_code_box).send_keys(promocode)
        self.driver.find_element(*self.promo_code_apply).click()

    def assert_promo_code_applied(self, promocodestatus):
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.presence_of_element_located(self.promo_code_applied_text)).is_displayed()
        promo_display_text = self.driver.find_element(*self.promo_code_applied_text).text

        assert promo_display_text == promocodestatus

    def click_place_order_button(self):
        self.driver.find_element(*self.place_order_button).click()
