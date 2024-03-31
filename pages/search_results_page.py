from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class SearchResultsPage(BasePage):

    PRODUCT_TITLE = (By.CLASS_NAME, "product-item-link")
    BUTTON_ADD_TO_CART = (By.CSS_SELECTOR, ".action.tocart.primary")
    BUTTON_SIZE = (By.ID, "option-label-size-143-item-176")
    BUTTON_COLOR =(By.ID, 'option-label-color-93-item-53')

    def verify_url(self):
        assert "https://magento.softwaretestingboard.com/catalogsearch/result/?q=troy" in self.driver.current_url

    def verify_search_results_displayed(self):
        results = self.find_all(self.PRODUCT_TITLE)
        assert len(results) > 0
    def click_size(self):
        self.find(self.BUTTON_SIZE).click()
    def click_color(self):
        self.find(self.BUTTON_COLOR).click()
    def click_add_to_cart(self):
        self.find(self.BUTTON_ADD_TO_CART).click()