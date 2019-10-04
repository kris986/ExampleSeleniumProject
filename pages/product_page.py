from selenium.webdriver.common.by import By
from .locators import ProductPagaLocators
from ExampleSeleniumProject.pages.base_page import BasePage


class ProductPage(BasePage):

    def add_product_to_basket(self):
        # Описать метод для добавления в корзину
        button = self.browser.find_element(*ProductPagaLocators.BUTTON_ADD_TO_BASKET)
        button.click()

    def should_be_product_page(self):
        self.should_be_product_url()
        self.should_be_product_info()
        self.should_be_wishlist_and_add_buttons()

    def should_be_product_url(self):
        pass

    def should_be_wishlist_and_add_buttons(self):
        assert self.is_element_presents(*ProductPagaLocators.BUTTON_ADD_TO_BASKET)
        assert self.is_element_presents(*ProductPagaLocators.BUTTON_ADD_TO_WISHLIST)

    def should_be_product_info(self):
        assert self.is_element_presents(*ProductPagaLocators.PRODUCT_GALLERY)
        assert self.is_element_presents(*ProductPagaLocators.PRODUCT_PRICE)
