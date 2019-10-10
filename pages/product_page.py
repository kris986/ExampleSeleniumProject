import re

from .locators import ProductPageLocators, BasePageLocators
from .base_page import BasePage


class ProductPage(BasePage):

    def add_product_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        button.click()

    def should_be_product_page(self):
        self.should_be_product_url()
        self.should_be_general_elems_on_page()
        self.should_be_product_info()
        self.should_be_wishlist_and_add_basket_buttons()

    def should_be_product_url(self):
        pattern = '(?:/catalogue/){1}(?:[0-9a-zA-Z/.=_-])+(?:[?0-9a-zA-Z=&]){0,}'
        current_url = self.browser.current_url
        match = re.search(pattern, current_url)
        assert match, 'Product URL is not correct'

    def should_be_wishlist_and_add_basket_buttons(self):
        assert self.is_element_presents(
            *ProductPageLocators.BUTTON_ADD_TO_BASKET), 'Button for addint to basket IS NOT present on page'
        assert self.is_element_presents(*ProductPageLocators.BUTTON_ADD_TO_WISHLIST_GUEST) or self.is_element_presents(
            *ProductPageLocators.BUTTON_ADD_TO_WISHLIST_USER), 'Button for adding to wishlist IS NOT present on page'

    def should_be_product_info(self):
        assert self.is_element_presents(*ProductPageLocators.PRODUCT_GALLERY), 'Product gallery IS NOT present on page'
        assert self.is_element_presents(*ProductPageLocators.PRODUCT_PRICE), 'Product price IS NOT present on page'
        assert self.is_element_presents(*ProductPageLocators.PRODUCT_TITLE), 'Product title IS NOT present on page'

    def should_be_msg_added_to_basket(self):
        assert self.is_element_presents(
            *ProductPageLocators.SUCCESS_MSG_ADDED_TO_BASKET), 'Success message about adding to basket IS NOT present on page'
        assert self.is_element_presents(
            *ProductPageLocators.ALERT_MSG_AMOUNT_BASKET), 'Amount of basket in alert message IS NOT present on page'
        product_title_in_success_msg = self.browser.find_element(*ProductPageLocators.SUCCESS_MSG_ADDED_TO_BASKET).text
        product_title = self.browser.find_element(*ProductPageLocators.PRODUCT_TITLE).text
        assert product_title == product_title_in_success_msg, 'Product title added to basket  IS NOT correct'

    def should_be_correct_amount_basket(self):
        pattern = r'(?:\d+.?\d*)'
        product_price = re.findall(pattern, self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text)[0]
        msg_amount_of_basket = \
            re.findall(pattern, self.browser.find_element(*ProductPageLocators.ALERT_MSG_AMOUNT_BASKET).text)[0]
        amount_of_basket_in_header = \
            re.findall(pattern, self.browser.find_element(*BasePageLocators.AMOUNT_OF_BASKET_IN_HEADER).text)[0]
        assert product_price == amount_of_basket_in_header, "Amount of basket IS NOT equal product's price"
        assert product_price == msg_amount_of_basket, "Amount of basket in alert message IS NOT equal product's price"

    def should_be_general_elems_on_page(self):
        assert self.is_element_presents(
            *BasePageLocators.AMOUNT_OF_BASKET_IN_HEADER), 'There IS NOT basket block in the header'

    def should_be_not_scs_msg_adding_to_basket(self):
        assert self.is_not_element_present(
            *ProductPageLocators.SUCCESS_MSG_ADDED_TO_BASKET), 'Success message about adding to basket iS present on page, but should not be'

    def should_disappear_success_msg(self):
        assert self.is_disappeared(
            *ProductPageLocators.SUCCESS_MSG_ADDED_TO_BASKET), 'Success message about adding to basket iS NOT disappeard from page'
