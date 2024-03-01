from pages_common.base_page import BasePage
import allure


class LeftMenuPage(BasePage):

    book_store_application_btn = '//*[text()="Book Store Application"]'
    login_bnt = '//*[text() = "Login"]'
    book_store_btn = '//*[text() = "Book Store"]'
    book_profile_btn = '//*[text() = "Profile"]'
    book_book_store_api_btn = '//*[text() = "Book Store API"]'
    practice_form_btn = '//span[text()="Practice Form"]'
    practice_form_btn_text = 'Practice Form'

    def __init__(self, page):
        super().__init__(page)



#click
    def click_practice_form_btn(self):
        with allure.step("click practice form btn"):
            self.click_by_text(self.practice_form_btn_text)
            return self

    def click_book_store_application_btn(self):
        with allure.step("click book store application btn"):
            self.click_by_locator(self.book_store_application_btn)
            return self

#check
    def check_practice_form_btn(self, locator: tuple):
        with allure.step("check practice form btn"):
            self.check_elm(locator)
            return self

    def check_login_btn(self, locator):
        with allure.step("check login btn"):
            self.check_elm(locator)
            return self

    def check_book_store_btn(self, locator):
        with allure.step("check book store btn"):
            self.check_elm(locator)
            return self

    def check_profile_btn(self, locator):
        with allure.step("check profile btn"):
            self.check_elm(locator)
            return self

    def check_book_store_api_btn(self, locator):
        with allure.step("check_book_store_api_btn"):
            self.check_elm(locator)
            return self








