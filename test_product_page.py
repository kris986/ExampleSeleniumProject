from datetime import datetime

import pytest

from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage


# var is used for tests that are not in Test's class
url_page = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


class TestUserAddToBasketFromProductPage:
    url_page = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, browser):
        email = datetime.now().strftime("%d.%m.%Y-%H-%M-%S-%f") + "@fakemail.org"
        password = 'ASD123456789'
        url_login_page = 'http://selenium1py.pythonanywhere.com/accounts/login/'
        self.registration_page = LoginPage(browser, url_login_page)
        self.registration_page.open()
        self.registration_page.register_new_user(email, password)

    @pytest.mark.need_review
    @pytest.mark.parametrize('link',
                             ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                              pytest.param(
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                                  marks=pytest.mark.xfail),
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
    def test_user_can_add_product_to_basket(self, browser, link):
        product_page = ProductPage(browser, f'{link}')
        product_page.open()
        product_page.should_be_product_page()
        product_page.add_product_to_basket()
        product_page.solve_quiz_and_get_code()
        product_page.should_be_msg_added_to_basket()
        product_page.should_be_correct_amount_basket()

    @pytest.mark.xfail
    def test_user_cant_see_success_message_after_adding_product_to_basket(self, browser):
        product_page = ProductPage(browser, url_page)
        product_page.open()
        product_page.should_be_product_page()
        product_page.add_product_to_basket()
        product_page.should_be_not_scs_msg_adding_to_basket()


@pytest.mark.need_review
@pytest.mark.parametrize('link',
                         ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                          pytest.param(
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                              marks=pytest.mark.xfail),
                          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, link):
    product_page = ProductPage(browser, f'{link}')
    product_page.open()
    product_page.should_be_product_page()
    product_page.add_product_to_basket()
    product_page.solve_quiz_and_get_code()
    product_page.should_be_msg_added_to_basket()
    product_page.should_be_correct_amount_basket()


def test_guest_cant_see_success_message(browser):
    product_page = ProductPage(browser, url_page)
    product_page.open()
    product_page.should_be_not_scs_msg_adding_to_basket()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    product_page = ProductPage(browser, url_page)
    product_page.open()
    product_page.should_be_product_page()
    product_page.add_product_to_basket()
    product_page.should_disappear_success_msg()


def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, url_page)
    page.open()
    page.should_be_login_link()


def test_message_disappeared_after_adding_product_to_basket(browser):
    product_page = ProductPage(browser, url_page)
    product_page.open()
    product_page.should_be_product_page()
    product_page.add_product_to_basket()
    product_page.should_disappear_success_msg()


def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, url_page)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    product_page = ProductPage(browser, url_page)
    product_page.open()
    product_page.should_be_product_page()
    product_page.should_be_login_link()
    product_page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    product_page = ProductPage(browser, url_page)
    product_page.open()
    product_page.should_be_basket_link()
    product_page.go_to_basket_from_header()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_basket_page()
    basket_page.should_be_empty_basket()
