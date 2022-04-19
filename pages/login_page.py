from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "login" in self.browser.current_url, "Link is not current"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email, password):
        self.input_value(*LoginPageLocators.REGISTRATION_EMAIL, email)
        self.input_value(*LoginPageLocators.REGISTRATION_PASSWORD_1, password)
        self.input_value(*LoginPageLocators.REGISTRATION_PASSWORD_2, password)
        self.element_click(*LoginPageLocators.REGISTRATION_BUTTON)
