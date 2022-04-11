import math
from .base_page import BasePage
from selenium.common.exceptions import NoAlertPresentException
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def add_to_basket(self):
        self.element_click(*ProductPageLocators.ADD_BUTTON)

    def assert_sum(self):
        assert self.element_value(*ProductPageLocators.PRICE) in self.element_value(
            *ProductPageLocators.SUM), "Sum is not correct"

    def assert_added_product_name(self):
        assert self.element_value(*ProductPageLocators.PRODUCT_NAME) == self.element_value(
            *ProductPageLocators.ADDED_PRODUCT), "Name is not correct"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_ADDED_PRODUCT_TEXT), \
            "Success message is presented, but should not be"

    def success_message_is_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_ADDED_PRODUCT_TEXT), \
            "Success message is not disappeared"
