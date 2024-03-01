from pages_common.base_page import BasePage
from playwright.sync_api import expect
import allure


class MainPage(BasePage):

    url = 'https://demoqa.com/'
    elements_btn = '//h5[text()="Elements"]'
    forms_btn = '//h5[text()="Forms"]'
    alerts_btn = '//h5[text()="Alerts, Frame & Windows"]'
    widget_btn = '//h5[text()="Widgets"]'
    interactions_btn = '//h5[text()="Interactions"]'
    book_store_btn = '//h5[text()="Book Store Application"]'
    link = '[href="https://www.toolsqa.com/selenium-training/"]'

    def __init__(self, page):
        super().__init__(page)

#open
    # def open(self, url):
    #     with allure.step("open main page"):
    #         self.open_page(url)

    def open(self):
        with allure.step("open main page"):
            self.open_page(self.url)
            return self

    async def open_async(self, url):
        await self.open_page_async(url)

#check
    def check_elements_btn(self, locator: str):
        with allure.step("check elements btn"):
            self.check_elm(locator)
            return self

    def check_forms_btn(self, locator: str):
        with allure.step("check forms btn"):
            self.check_elm(locator)
            return self

    def check_alerts_btn(self, locator: tuple):
        with allure.step("check alerts btn"):
            self.check_elm(locator)
            return self

    def check_widget_btn(self, locator: tuple):
        with allure.step("check widget btn"):
            self.check_elm(locator)
            return self

    def check_interactions_btn(self, locator: tuple):
        with allure.step("check interactions btn"):
            self.check_elm(locator)
            return self

    def check_book_store_btn(self, locator: tuple):
        with allure.step("check book store btn"):
            self.check_elm(locator)
            return self

    def check_link(self, locator: tuple):
        with allure.step("check link"):
            self.check_elm(locator)

#click
    def click_elements_btn(self):
        with allure.step("click elements btn"):
            self.click_by_locator(self.elements_btn)
            return self

    def click_forms_btn(self):
        with allure.step("click forms btn"):
            self.click_by_locator(self.forms_btn)
            return self

    def click_alerts_btn(self):
        with allure.step("click alerts btn"):
            self.click_by_locator(self.alerts_btn)
            return self

    def click_widget_btn(self):
        with allure.step("click widget btn"):
            self.click_by_locator(self.widget_btn)
            return self

    def click_interactions_btn(self):
        with allure.step("click interactions btn"):
            self.click_by_locator(self.interactions_btn)
            return self

    def click_book_store_btn(self):
        with allure.step("click book store btn"):
            self.click_by_locator(self.book_store_btn)
            return self
















