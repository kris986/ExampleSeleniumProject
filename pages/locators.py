from selenium.webdriver.common.by import By


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
