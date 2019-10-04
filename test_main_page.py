class MainPage:

    def test_guest_can_go_to_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        browser.get(link)
        self.go_to_login_page(browser)

    def go_to_login_page(self, browser):
        link = browser.find_element_by_css_selector("#login_link")
        link.click()
