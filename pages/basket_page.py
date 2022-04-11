from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_basket_empty_text(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_TEXT), "Basket is not empty"

    def should_not_be_product(self):
        assert self.is_not_element_present(*BasketPageLocators.NOT_EMPTY_BASKET_TEXT), "Basket is empty"
