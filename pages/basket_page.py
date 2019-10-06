from .base_page import BasePage


class BasketPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(BasketPage, self).__init__(*args, **kwargs)

    def should_be_basket_page(self):
        pass

    def should_be_empty_basket(self):
        pass

    def should_be_not_total_basket_block(self):
        pass
