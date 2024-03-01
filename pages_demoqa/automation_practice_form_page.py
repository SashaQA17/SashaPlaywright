from pages_common.base_page import BasePage
from playwright.sync_api import expect
import allure


class AutomationPracticeFormPage(BasePage):

    url = 'https://demoqa.com/automation-practice-form'
    practice_form = '//h1[@class="text-center"]'
    first_name = '//input[@id="firstName"]'
    last_name = '//input[@id="lastName"]'
    email = '//input[@id="userEmail"]'
    male = '//*[contains(text(), "Male")]'

    def __init__(self, page):
        super().__init__(page)


#open
    def open(self):
        with allure.step("open automation practice form page"):
            self.open_page(self.url)
            return self

#check
    def check_main_text(self, locator: tuple):
        with allure.step("check the main text"):
            self.check_elm(locator)
            return self

#click
    def select_gender(self, locator: tuple):
        with allure.step("select gender"):
            self.click_by_locator(locator)
            return self

#fill_in
    def fill_in_first_name(self, text: str):
        with allure.step("fill in first name"):
            self.fill_in_by_locator(self.first_name, text)
            return self

    def fill_in_last_name(self, text: str):
        with allure.step("fill in last name"):
            self.fill_in_by_locator(self.last_name, text)
            return self

    def fill_in_email(self, text: str):
        with allure.step("fill in email"):
            self.fill_in_by_locator(self.email, text)
            return self

