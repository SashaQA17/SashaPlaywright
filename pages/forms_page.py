from pages.base_page import BasePage
from playwright.sync_api import expect
import allure


class FormsPage(BasePage):

    url = 'https://demoqa.com/forms'
    practice_form_btn = '//span[text()="Practice Form"]'
    practice_form_btn_text = 'Practice Form'

    def __init__(self, page):
        super().__init__(page)


#open
    def open(self):
        with allure.step("open form page"):
            self.open_page(self.url)
            return self


#check
    def check_practice_form_btn(self, locator: tuple):
        with allure.step("check practice form btn"):
            self.check_elm(locator)
            return self


#click
    def click_practice_form_btn(self):
        with allure.step("click practice form btn"):
            self.click_by_locator(self.practice_form_btn)
        return self

