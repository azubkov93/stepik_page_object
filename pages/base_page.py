from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from .locators import BasePageLocators


class BasePage:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_not_element_present(self, how, what, timeout=4):
        # элемент не появляется на странице в течение заданного времени
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def is_disappeared(self, how, what, timeout=4):
        # элемент исчезает
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def element_click(self, how, what):
        try:
            element = self.browser.find_element(how, what)
            element.click()
        except NoSuchElementException:
            return "element not found"

    def input_value(self, how, what, text):
        try:
            element = self.browser.find_element(how, what)
            element.send_keys(text)
        except NoSuchElementException:
            return "element not found"

    def element_value(self, how, what):
        try:
            element = self.browser.find_element(how, what).text
            return element
        except NoSuchElementException:
            return "element not found"

    def go_to_login_page(self):
        try:
            link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
            link.click()
        except NoSuchElementException:
            return "element not found"

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    def go_to_basket_page(self):
        try:
            link = self.browser.find_element(*BasePageLocators.BASKET_LINK)
            link.click()
        except NoSuchElementException:
            return "element not found"

    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," \
                                                                     " probably unauthorised user"
