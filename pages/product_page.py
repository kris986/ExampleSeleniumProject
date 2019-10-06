import re
from .locators import ProductPagaLocators
from ExampleSeleniumProject.pages.base_page import BasePage


class ProductPage(BasePage):

    def add_product_to_basket(self):
        # Описать метод для добавления в корзину
        button = self.browser.find_element(*ProductPagaLocators.BUTTON_ADD_TO_BASKET)
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
        assert self.is_element_presents(*ProductPagaLocators.BUTTON_ADD_TO_BASKET)
        assert self.is_element_presents(*ProductPagaLocators.BUTTON_ADD_TO_WISHLIST)

    def should_be_product_info(self):
        assert self.is_element_presents(*ProductPagaLocators.PRODUCT_GALLERY), 'Product gallery is not present on page'
        assert self.is_element_presents(*ProductPagaLocators.PRODUCT_PRICE), 'Product price is not present on page'
        assert self.is_element_presents(*ProductPagaLocators.PRODUCT_TITLE), 'Product title is not present on page'

    def should_be_msg_added_to_basket(self):
        assert self.is_element_presents(
            *ProductPagaLocators.SUCCESS_MSG_ADDED_TO_BASKET), 'Success message about adding to basket is not present on page'
        assert self.is_element_presents(
            *ProductPagaLocators.ALERT_MSG_AMOUN_BASKET), 'Amount of basket in alert message is not present on page'
        product_title_in_success_msg = self.browser.find_element(*ProductPagaLocators.SUCCESS_MSG_ADDED_TO_BASKET).text
        product_title = self.browser.find_element(*ProductPagaLocators.PRODUCT_TITLE).text
        assert product_title == product_title_in_success_msg, 'Product title added to basket  is not correct'

    def should_be_correct_amount_basket(self):
        pattern = r'(?:\d+.?\d*)'
        product_price = re.findall(pattern, self.browser.find_element(*ProductPagaLocators.PRODUCT_PRICE).text)[0]
        msg_amount_of_basket = \
            re.findall(pattern, self.browser.find_element(*ProductPagaLocators.ALERT_MSG_AMOUN_BASKET).text)[0]
        amount_of_basket_in_header = \
            re.findall(pattern, self.browser.find_element(*ProductPagaLocators.AMOUNT_OF_BASKET_IN_HEADER).text)[0]
        assert product_price == amount_of_basket_in_header, "Amount of basket is not equal product's price"
        assert product_price == msg_amount_of_basket, "Amount of basket in alert message is not equal product's price"

    def should_be_general_elems_on_page(self):
        assert self.is_element_presents(
            *ProductPagaLocators.AMOUNT_OF_BASKET_IN_HEADER), 'There is not basket block in the header'
