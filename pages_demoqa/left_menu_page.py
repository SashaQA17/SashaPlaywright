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
    @allure.step("click practice form btn")
    def click_practice_form_btn(self):
        self.click_by_text(self.practice_form_btn_text)
        return self

    @allure.step("click book store application btn")
    def click_book_store_application_btn(self):
        self.click_by_locator(self.book_store_application_btn)
        return self

#check
    @allure.step("check practice form btn")
    def check_practice_form_btn(self, locator: tuple):
        self.check_elm(locator)
        return self

    @allure.step("check login btn")
    def check_login_btn(self, locator):
        self.check_elm(locator)
        return self

    @allure.step("check book store btn")
    def check_book_store_btn(self, locator):
        self.check_elm(locator)
        return self

    @allure.step("check profile btn")
    def check_profile_btn(self, locator):
        self.check_elm(locator)
        return self

    @allure.step("check_book_store_api_btn")
    def check_book_store_api_btn(self, locator):
        self.check_elm(locator)
        return self








