from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):

    LOGIN_PAGE_URL = "https://magento.softwaretestingboard.com/customer/account/login"
    INPUT_EMAIL = (By.ID, "email")
    INPUT_PASSWORD = (By.ID, "pass")
    BUTTON_SIGNIN = (By.ID, "send2")
    DIV_ERROR_MESSAGE = (By.CLASS_NAME, "message-error")

    def open(self):
        self.driver.get(self.LOGIN_PAGE_URL)
    def verify_url(self):
        assert self.driver.current_url == self.LOGIN_PAGE_URL
    def set_email(self, text):
        self.type(self.INPUT_EMAIL, text)
    def set_password(self, text):
        self.type(self.INPUT_PASSWORD, text)
    def click_signin_button(self):
        self.find(self.BUTTON_SIGNIN).click()
    def verify_signin_error_message(self, text):
        assert text in self.find(self.DIV_ERROR_MESSAGE).text