from pages.base_page import BasePage


class WhatsNewPage(BasePage):

    WHATS_NEW_PAGE_URL = "https://magento.softwaretestingboard.com/what-is-new.html"


    def open(self):
        self.driver.get(self.WHATS_NEW_PAGE_URL)

    def verify_url(self):
        assert self.driver.current_url == self.WHATS_NEW_PAGE_URL