from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
import browser
from pages.base_page import BasePage

import time
class SearchResultsPage(BasePage):

    BUTTON_ALL_REVIEWS = (By.CSS_SELECTOR, ".action.view")
    INPUT_YOUR_RATING = (By.ID, "Rating_5_label")
    INPUT_ALIAS = (By.ID, "nickname_field")
    INPUT_SUMMARY = (By.ID, "summary_field")
    INPUT_REVIEW = (By.ID, "review_field")
    BUTTON_SUBMIT_THE_REVIEW = (By.CSS_SELECTOR, ".action.submit")

    PRODUCT_TITLE = (By.CLASS_NAME, "product-item-link")
    BUTTON_ADD_TO_CART = (By.CSS_SELECTOR, ".action.tocart.primary")
    BUTTON_SELECT_SIZE = (By.ID, "option-label-size-143-item-176")
    BUTTON_SELECT_COLOR =(By.ID, 'option-label-color-93-item-53')
    BUTTON_SHOW_CART =(By.CSS_SELECTOR, '.action.showcart')
    BUTTON_CHECKOUT = (By.ID, 'top-cart-btn-checkout')
    INPUT_STREET = (By.NAME, 'street[0]')
    INPUT_CITY =(By.NAME, 'city')
    SELECT_STATE = (By.NAME, 'region_id')
    INPUT_POSTCODE =(By.NAME, 'postcode')
    SELECT_COUNTRY =(By.NAME, 'country_id')
    INPUT_TELEPHONE =(By.NAME, 'telephone')
    SHIPPING_METHODS =(By.NAME, 'ko_unique_1')
    BUTTON_CONTINUE =(By.CLASS_NAME, 'continue')
    CHECK_BILLING = (By.CLASS_NAME, "checkout-billing-address")
    BUTTON_PLACE_ORDER = (By.CSS_SELECTOR, '.action.primary.checkout')
    MESSAGE_ORDER_SUCCESS = (By.CLASS_NAME, "page-title")

    def verify_url(self):
        assert "https://magento.softwaretestingboard.com/catalogsearch/result/?q=tees" in self.driver.current_url

    def click_review_button(self):
        self.find(self.BUTTON_ALL_REVIEWS).click()

    def click_rating_rev(self):
        button_raiting = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(self.INPUT_YOUR_RATING))

        self.driver.execute_script("arguments[0].scrollIntoView();", button_raiting)

        ActionChains(self.driver).move_to_element(button_raiting).click().perform()

    def set_nickname(self, text):
        self.type(self.INPUT_ALIAS, text)
    def set_summary(self, text):
        self.type(self.INPUT_SUMMARY, text)
    def set_review(self, text):
        self.type(self.INPUT_REVIEW, text)
    def click_submit_review_button(self):
        self.find(self.BUTTON_SUBMIT_THE_REVIEW).click()


    def verify_search_results_displayed(self):
        results = self.find_all(self.PRODUCT_TITLE)
        assert len(results) > 0

    def click_size(self):
        self.find(self.BUTTON_SELECT_SIZE).click()
    def click_color(self):
        self.find(self.BUTTON_SELECT_COLOR).click()
    def click_add_to_cart(self):
        self.driver.implicitly_wait(8)
        self.find(self.BUTTON_ADD_TO_CART).click()

    def click_cart(self):
        button_cart = WebDriverWait(self.driver, 40).until(EC.element_to_be_clickable(self.BUTTON_SHOW_CART))
        button_cart.click()

    def click_proceed_checkout(self):
        button_checkout = WebDriverWait(self.driver, 40).until(EC.element_to_be_clickable(self.BUTTON_CHECKOUT))
        button_checkout.click()
        time.sleep(5)
    def verify_url_shipping(self, expected_url):
        current_url = self.driver.current_url
        print("URL-ul curent:", current_url)
        print("URL-ul asteptat:", expected_url)

        assert self.driver.current_url == expected_url
    def set_street_address(self, text):
        self.type(self.INPUT_STREET, text)

    def set_city(self, text):
        self.type(self.INPUT_CITY, text)

    def select_state(self, text):
        dropdown = self.find(self.SELECT_STATE)
        Select(dropdown).select_by_visible_text(text)

    def set_postal_code(self, number):
        self.type(self.INPUT_POSTCODE, number)

    def select_country(self, text):
        dropdown = self.find(self.SELECT_COUNTRY)
        Select(dropdown).select_by_visible_text(text)

    def set_phone_number(self, text):
        self.type(self.INPUT_TELEPHONE, text)

    def click_shipping_methods(self):
        self.find(self.SHIPPING_METHODS).click()

    def click_next_button(self):
        self.find(self.BUTTON_CONTINUE).click()

    def verify_url_payment(self, expected_url):
        current_url = self.driver.current_url
        print("URL-ul curent:", current_url)

        print("URL-ul asteptat:", expected_url)
        assert self.driver.current_url == expected_url

    def click_check_bill_address(self):
        self.find(self.CHECK_BILLING).click()
    def click_place_order_button(self):
        self.driver.implicitly_wait(8)
        self.find(self.BUTTON_PLACE_ORDER).click()

    def verify_url_order(self, expected_url):
        current_url = self.driver.current_url
        print("URL-ul curent:", current_url)

        print("URL-ul asteptat:", expected_url)
        assert self.driver.current_url == expected_url
    def verify_success_message_displayed(self):
        self.driver.implicitly_wait(8)
        assert self.find(self.MESSAGE_ORDER_SUCCESS).is_displayed()

    def verify_success_message_contains_text(self, text):
        success_message = self.find(self.MESSAGE_ORDER_SUCCESS).text
        print("Mesajul de succes actual este:", success_message)
        print("Textul asteptat este:", text)
        assert success_message == text
