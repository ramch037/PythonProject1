from checkout_page import CheckoutPage
from order_page import OrderPage
from product_page import ProductPage


def test_e2e(test_browser_setup_teardown):
    driver = test_browser_setup_teardown
    product_page = ProductPage(driver)
    product_page.search_product()
    product_page.add_items()
    product_page.click_cart_button()
    product_page.click_proceed_to_checkout()

    checkout_page = CheckoutPage(driver)
    checkout_page.enter_promo_code_apply('rahulshettyacademy')
    checkout_page.assert_promo_code_applied('Code applied ..!')
    checkout_page.click_place_order_button()

    order_page = OrderPage(driver)
    order_page.select_country('Afghanistan')
    order_page.select_country('Indi')
    order_page.select_checkbox_terms_conditions()
    order_page.click_proceed_button()
