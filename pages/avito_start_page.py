from pages.base_page import BasePage
from playwright.sync_api import expect
import allure


class AvitoStartPage(BasePage):

    url = 'https://www.avito.ru/penza/transport?cd=1'
    all_category_btn ='//button[@data-marker="top-rubricator/all-categories"]'
    orgtehnika_and_rashodniki_btn = '//strong[@data-cid="99"]'
    electronika_btn = '//p[text()="Электроника"]'


    def __init__(self, page):
        super().__init__(page)

#open
    def open(self):
        with allure.step("open first link"):
            self.open_page(self.url)
            return self

#click
    def click_all_category_btn(self):
        with allure.step("click all category btn"):
            self.click_by_locator(self.all_category_btn)
            return self

    def click_electronika_btn(self):
        with allure.step("click electonika btn"):
            self.click_by_locator(self.electronika_btn)
            return self

    def click_org_and_rash_btn(self):
        with allure.step("click orgtehnika and rashodniki btn"):
            self.click_by_locator(self.orgtehnika_and_rashodniki_btn)
            return self



