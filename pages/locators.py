from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    AMOUNT_OF_BASKET_IN_HEADER = (By.CSS_SELECTOR, 'div.basket-mini')


class LocatorsMainPage:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, 'form#login_form')
    LOGIN_INPUT_EMAIL = (By.CSS_SELECTOR, 'input#id_login-username')
    LOGIN_INPUT_PASSWORD = (By.CSS_SELECTOR, 'input#id_login-password')
    LOGIN_BUTTON_SUBMIT = (By.CSS_SELECTOR, 'button[name="login_submit"]')
    REGISTRATION_FORM = (By.CSS_SELECTOR, 'form#register_form')
    REGISTRATION_INPUT_EMAIL = (By.CSS_SELECTOR, 'input#id_registration-email')
    REGISTRATION_INPUT_PASSWORD = (By.CSS_SELECTOR, 'input#id_registration-password1')
    REGISTRATION_REPEAT_INPUT_PASSWORD = (By.CSS_SELECTOR, 'input#id_registration-password2')
    REGISTRATION_BUTTON_SUBMIT = (By.CSS_SELECTOR, 'button[name="registration_submit"]')


class ProductPagaLocators:
    PRODUCT_TITLE = (By.CSS_SELECTOR, 'div.product_main > h1')
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, 'form#add_to_basket_form > button.btn-add-to-basket')
    BUTTON_ADD_TO_WISHLIST = (By.CSS_SELECTOR, 'button.btn.btn-lg.btn-wishlist')
    PRODUCT_GALLERY = (By.CSS_SELECTOR, 'div#product_gallery')
    PRODUCT_PRICE = (By.CSS_SELECTOR, 'div.product_main > p.price_color')
    SUCCESS_MSG_ADDED_TO_BASKET = (By.CSS_SELECTOR, 'div#messages div.alert-success:nth-child(1) strong')
    ALERT_MSG_AMOUN_BASKET = (By.CSS_SELECTOR, 'div#messages div.alert-info strong')

