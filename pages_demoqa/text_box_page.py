from pages_common.base_page import BasePage
from data.generate_person import generate
from data.data_person import Person
from playwright.sync_api import Page, expect


import allure

class TextBox(BasePage):

    url = 'https://demoqa.com/text-box'
    h1_text = '//h1[contains(text(),"Text Box")]'
    name_answer = '//p[@id="name"]'
    # full_name_text = '//label[contains(text(),"Full Name")]'
    # email_text = '//label[contains(text(),"Email")]'
    # cur_address_text = '//label[contains(text(),"Current Address")]'
    # per_address_text = '//label[contains(text(),"Permanent Address")]'
    name_field = '//input[@id="userName"]'
    email_field = '//input[@id="userEmail"]'
    cur_address_field = '//*[@id="currentAddress"]'
    per_address_field = '//*[@id="permanentAddress"]'
    submit_btn = '//button[@id="submit"]'


    def __init__(self, page):
        super().__init__(page)

#open
    def open(self):
        with allure.step("open text-box page"):
            self.open_page(self.url)
            return self

#check
    def check_main_text(self):
        with allure.step("check the main text"):
            self.check_elm(self.h1_text)
            return self

    # def check_full_name_text(self):
    #     with allure.step("check full name text"):
    #         self.check_elm(self.full_name_text)
    #         return self
    #
    # def check_email_text(self):
    #     with allure.step("check email text"):
    #         self.check_elm(self.email_text)
    #         return self
    #
    # def check_cur_address_text(self):
    #     with allure.step("check current address text"):
    #         self.check_elm(self.cur_address_text)
    #         return self
    #
    # def check_per_address_text(self):
    #     with allure.step("check permanent address text"):
    #         self.check_elm(self.per_address_text)
    #         return self

    def check_subtitle_text(self, name_text):
        with allure.step(f"check {name_text} text"):
            self.check_elm(f'//label[contains(text(),"{name_text}")]')
            return self

    # def check_name_field(self):
    #     with allure.step("check name field"):
    #         self.check_elm(self.name_field)
    #         return self
    #
    # def check_submit_btn(self):
    #     with allure.step("check submit btn"):
    #         self.check_elm(self.submit_btn)
    #         return self

    def check_field_and_btn(self, field_name):
        with allure.step(f"check {field_name} field"):
            self.check_elm(f'//*[@id="{field_name}"]')
            return self


    def check_answer(self, text):
        with allure.step("check answer"):
            elem = self.get_text(self.name_answer)
            assert elem == text

#click
    def click_submit_btn(self):
        with allure.step("click submit btn"):
            self.click_by_locator(self.submit_btn)
            return self

#fill_in
    def fill_in_name_field(self, text):
        with allure.step("fill in name field"):
            self.fill_in_by_locator(self.name_field, text)
            return self

    def fill_in_email_field(self, text):
        with allure.step("fill in email field"):
            self.fill_in_by_locator(self.email_field, text)
            return self

    def fill_in_cur_address_field(self, text):
        with allure.step("fill in current address field"):
            self.fill_in_by_locator(self.cur_address_field, text)
            return self

    def fill_in_per_address_field(self, text):
        with allure.step("fill in permanent address field"):
            self.fill_in_by_locator(self.per_address_field, text)
            return self

#functional
    def fill_in_form(self, text1: str, text2: str, text3: str, text4: str):
        with allure.step("fill_in_form"):
            self.fill_in_name_field(text1)
            self.fill_in_email_field(text2)
            self.fill_in_cur_address_field(text3)
            self.fill_in_per_address_field(text4)
            self.click_submit_btn()
            return self
