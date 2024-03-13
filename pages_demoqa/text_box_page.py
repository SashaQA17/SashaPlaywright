from pages_common.base_page import BasePage
from data.generate_person import generate
from data.data_person import Person
from playwright.sync_api import Page, expect
import allure


class TextBox(BasePage):

    url = 'https://demoqa.com/text-box'
    h1_text = '//h1[contains(text(),"Text Box")]'
    name_answer = '//p[@id="name"]'
    name_field = '//input[@id="userName"]'
    email_field = '//input[@id="userEmail"]'
    cur_address_field = '//*[@id="currentAddress"]'
    per_address_field = '//*[@id="permanentAddress"]'
    submit_btn = '//button[@id="submit"]'

    def __init__(self, page):
        super().__init__(page)


#open
    @allure.step("open text-box page")
    def open(self):
        self.open_page(self.url)
        return self

#check
    @allure.step("check the main text")
    def check_main_text(self):
        self.check_elm(self.h1_text)
        return self

    @allure.step("check {name_text} text")
    def check_subtitle_text(self, name_text):
        self.check_elm(f'//label[contains(text(),"{name_text}")]')
        return self

    @allure.step("check {field_name} field")
    def check_field_and_btn(self, field_name):
        self.check_elm(f'//*[@id="{field_name}"]')
        return self

    @allure.step("check answer")
    def check_answer(self, text):
        elem = self.get_text(self.name_answer)
        assert elem == text

#click
    @allure.step("click submit btn")
    def click_submit_btn(self):
        self.click_by_locator(self.submit_btn)
        return self

#fill_in
    @allure.step("fill in name field")
    def fill_in_name_field(self, text):
        self.fill_in_by_locator(self.name_field, text)
        return self

    @allure.step("fill in email field")
    def fill_in_email_field(self, text):
        self.fill_in_by_locator(self.email_field, text)
        return self

    @allure.step("fill in current address field")
    def fill_in_cur_address_field(self, text):
        self.fill_in_by_locator(self.cur_address_field, text)
        return self

    @allure.step("fill in permanent address field")
    def fill_in_per_address_field(self, text):
        self.fill_in_by_locator(self.per_address_field, text)
        return self

#functional
    @allure.step("fill_in_form")
    def fill_in_form(self, text1: str, text2: str, text3: str, text4: str):
        self.fill_in_name_field(text1)  # Заполнить имя
        self.fill_in_email_field(text2)  # Заполнить эмейл
        self.fill_in_cur_address_field(text3)  # Заполнить текущий адрес
        self.fill_in_per_address_field(text4)   # Заполнить действуйщий адрес
        self.click_submit_btn()  # Нажать кнопку подтвердить
        return self
