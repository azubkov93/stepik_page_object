import pytest
from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage


# @pytest.mark.parametrize('link',
#                          ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
#                           "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
#                           "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
#                           "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
#                           "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
#                           "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
#                           "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
#                           pytest.param(
#                               "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
#                               marks=pytest.mark.xfail),
#                           "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
#                           "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
# def test_guest_can_add_product_to_basket(browser, link):
#     page = ProductPage(browser, link)
#     page.open()
#     page.add_to_basket()
#     page.solve_quiz_and_get_code()
#     page.assert_added_product_name()
#     page.assert_sum()


def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    page.open()
    page.add_to_basket()
    page.should_not_be_success_message()


# Открываем страницу товара
# Добавляем товар в корзину
# Проверяем, что нет сообщения об успехе с помощью is_not_element_present


def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    page.open()
    page.should_not_be_success_message()


# Открываем страницу товара
# Проверяем, что нет сообщения об успехе с помощью is_not_element_present


def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    page.open()
    page.add_to_basket()
    page.success_message_is_disappeared()


# Открываем страницу товара
# Добавляем товар в корзину
# Проверяем, что нет сообщения об успехе с помощью is_disappeared

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "https://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_product()
    basket_page.should_be_basket_empty_text()


# Гость открывает страницу товара
# Переходит в корзину по кнопке в шапке
# Ожидаем, что в корзине нет товаров
# Ожидаем, что есть текст о том что корзина пуста

# @pytest.mark.login
# class TestLoginFromProductPage:
#     @pytest.fixture(scope="function", autouse=True)
#     def setup(self):
#         self.product = ProductFactory(title="Best book created by robot")
#         # создаем по апи
#         self.link = self.product.link
#         yield
#         # после этого ключевого слова начинается teardown
#         # выполнится после каждого теста в классе
#         # удаляем те данные, которые мы создали
#         self.product.delete()
#
#     def test_guest_can_go_to_login_page_from_product_page(self, browser):
#         page = ProductPage(browser, self.link)
#         # дальше обычная реализация теста
#
#     def test_guest_should_see_login_link(self, browser):
#         page = ProductPage(browser, self.link)
#         # дальше обычная реализация теста
