from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        url = self.browser.current_url
        assert url.find('/login/') != -1, 'Login URL is not correct'

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_presents(*LoginPageLocators.LOGIN_FORM), 'Login Form is not presented'
        assert self.is_element_presents(*LoginPageLocators.LOGIN_INPUT_EMAIL), 'Email input for login  is not presented'
        assert self.is_element_presents(
            *LoginPageLocators.LOGIN_INPUT_PASSWORD), 'Password input for login  is not presented'
        assert self.is_element_presents(
            *LoginPageLocators.LOGIN_BUTTON_SUBMIT), 'Submit button for login  is not presented'

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_presents(*LoginPageLocators.REGISTRATION_FORM), 'Registration Form is not presented'
        assert self.is_element_presents(
            *LoginPageLocators.REGISTRATION_INPUT_EMAIL), 'Email input for registration  is not presented'
        assert self.is_element_presents(
            *LoginPageLocators.REGISTRATION_INPUT_PASSWORD), 'Password input for registration  is not presented'
        assert self.is_element_presents(
            *LoginPageLocators.REGISTRATION_REPEAT_INPUT_PASSWORD), 'Reapeat password input for registration  is not presented'
        assert self.is_element_presents(
            *LoginPageLocators.REGISTRATION_BUTTON_SUBMIT), 'Submit button for registration  is not presented'
