from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.ID, "login_form")
    LOGIN_USERNAME = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "#id_login-password")
    RESTORE_PASSWORD_LINK = (By.LINK_TEXT, "Я забыл пароль")
    LOGIN_BUTTON = (By.NAME, "login_submit")

    REGISTER_FORM = (By.ID, "register_form")
    REGISTRATION_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTRATION_PASSWORD_1 = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTRATION_PASSWORD_2 = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTRATION_BUTTON = (By.NAME, "registration_submit")


class ProductPageLocators:
    ADD_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRICE = (By.CSS_SELECTOR, ".product_main>p.price_color")
    SUM = (By.CSS_SELECTOR, ".basket-mini")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main>h1")
    ADDED_PRODUCT = (By.CSS_SELECTOR, ".alertinner>strong")
    SUCCESS_ADDED_PRODUCT_TEXT = (By.CSS_SELECTOR, ".alertinner>strong")


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini a.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators:
    EMPTY_BASKET_TEXT = (By.CSS_SELECTOR, "#content_inner p")
    NOT_EMPTY_BASKET_TEXT = (By.CSS_SELECTOR, ".basket-title h2")
