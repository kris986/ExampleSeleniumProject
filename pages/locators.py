from selenium.webdriver.common.by import By


class BasePageLocators:
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    AMOUNT_OF_BASKET_IN_HEADER = (By.CSS_SELECTOR, 'div.basket-mini')
    BASKET_LINK = (By.CSS_SELECTOR, 'div.basket-mini > span a')
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    PAGE_HEADER = (By.CSS_SELECTOR, 'div.page-header h1')


class BasketPageLocators:
    BASKET_SUMMARY_FORM = (By.CSS_SELECTOR, 'form#basket_formset')
    # "Continue shopping" link is used as a marker of empty basket
    MESSAGE_CONTINIE_SHOPPING = (By.CSS_SELECTOR, 'div#content_inner>p>a')


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


class ProductPageLocators:
    ALERT_MSG_AMOUNT_BASKET = (By.CSS_SELECTOR, 'div#messages div.alert-info strong')
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, 'form#add_to_basket_form > button.btn-add-to-basket')
    BUTTON_ADD_TO_WISHLIST_GUEST = (By.CSS_SELECTOR, 'button.btn.btn-lg.btn-wishlist')
    BUTTON_ADD_TO_WISHLIST_USER = (By.CSS_SELECTOR, 'form#add_to_wishlist_form button.btn.btn-lg')
    PRODUCT_TITLE = (By.CSS_SELECTOR, 'div.product_main > h1')
    PRODUCT_GALLERY = (By.CSS_SELECTOR, 'div#product_gallery')
    PRODUCT_PRICE = (By.CSS_SELECTOR, 'div.product_main > p.price_color')
    SUCCESS_MSG_ADDED_TO_BASKET = (By.CSS_SELECTOR, 'div#messages div.alert-success:nth-child(1) strong')
