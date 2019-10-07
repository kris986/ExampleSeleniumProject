from .locators import BasePageLocators, BasketPageLocators

from .base_page import BasePage


class BasketPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(BasketPage, self).__init__(*args, **kwargs)

    def should_be_basket_page(self):
        self.should_be_basket_url()
        self.should_be_basket_head()

    def should_be_basket_url(self):
        page_url = self.browser.current_url
        assert page_url.find('/basket/') != -1, 'Basket URL is not correct'

    def should_be_basket_head(self):
        assert self.is_element_presents(*BasePageLocators.PAGE_HEADER), 'Header of basket IS NOT present on page'


    def should_be_empty_basket(self):
        self.should_be_msg_about_empty_basket(),  'Message about empty  basket IS NOT present on page'
        self.should_not_be_summury_of_order(), 'Message about empty  basket IS NOT present on page'

    def should_not_be_empty_basket(self):
        assert self.is_element_presents(*BasketPageLocators.BASKET_SUMMARY_FORM)
        assert self.should_not_be_msg_about_empty_basket()

    def should_not_be_summury_of_order(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_SUMMARY_FORM), 'Summary of order IS present on page, but should not'

    def should_be_msg_about_empty_basket(self):
        assert self.is_element_presents(*BasketPageLocators.MESSAGE_CONTINIE_SHOPPING)

    def should_not_be_msg_about_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.MESSAGE_CONTINIE_SHOPPING)
