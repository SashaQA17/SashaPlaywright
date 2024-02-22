from pages.base_page import BasePage
from playwright.sync_api import Page, expect
import allure


class AvitoOrgtehnika(BasePage):

    url = 'https://www.avito.ru/penza/orgtehnika_i_rashodniki'
    search_field = '//input[@data-marker ="search-form/suggest"]'
    region_btn = '//div[@data-marker="search-form/change-location"]'
    region_field = '//input[@placeholder = "Город или регион"]'
    first_item = '//ul[@data-marker="suggest-list"]/li[1]//strong'
    show_result_btn = '//button[@type="button"]/span[contains(text(), "Показать")]'
    sort_btn = '//*[@id="app"]//div[1]/div[2]/div/span[text()="Сортировка"]'
    expensive_btn = '//div[text()="Дороже"]'
    price = '//strong[@class="styles-module-root-LIAav"]/span'

    def __init__(self, page):
        super().__init__(page)

#open
    def open(self):
        with allure.step("open orgtehnika page"):
            self.open_page(self.url)
            return self

#click
    def click_select_region(self):
        with allure.step("click select region btn"):
            self.click_by_locator(self.region_btn)
            return self

    def select_first_item(self):
        with allure.step("select first item"):
            self.click_by_locator(self.first_item)
            return self

    def click_show_result(self):
        with allure.step("click show result btn"):
            self.click_by_locator(self.show_result_btn)
            return self

    def click_sort_btn(self):
        with allure.step("click sort btn"):
            self.click_by_locator(self.sort_btn)
            return self

    def click_expensive_btn(self):
        with allure.step("click expensive btn"):
            self.click_by_locator((self.expensive_btn))
            return self

#fill_in
    def fill_in_search_field(self, text: str):
        with allure.step("fill in search field"):
            self.fill_in_by_locator(self.search_field, text)
            return self

    def fill_in_region_field(self, text: str):
        with allure.step("fill in search field"):
            self.clear_and_fill_in(self.region_field, text)
            return self

#check price
    def check_price(self):
        with allure.step("check price"):
            self.print_text()



