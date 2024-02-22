from pages.base_page import BasePage
from playwright.sync_api import expect
import allure


class FormsPage(BasePage):

    url = 'https://demoqa.com/forms'

    def __init__(self, page):
        super().__init__(page)

#open
    def open(self):
        with allure.step("open form page"):
            self.open_page(self.url)
            return self

#check

#click




