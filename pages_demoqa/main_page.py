from pages_common.base_page import BasePage
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
    @allure.step("open main page")
    def open(self):
        self.open_page(self.url)
        return self

    async def open_async(self, url):
        await self.open_page_async(url)

#check
    @allure.step("check elements btn")
    def check_elements_btn(self, locator: str):
        self.check_elm(locator)
        return self


    @allure.step("check forms btn")
    def check_forms_btn(self, locator: str):
        self.check_elm(locator)
        return self

    @allure.step("check alerts btn")
    def check_alerts_btn(self, locator: tuple):
        self.check_elm(locator)
        return self

    @allure.step("check widget btn")
    def check_widget_btn(self, locator: tuple):
        self.check_elm(locator)
        return self


    @allure.step("check interactions btn")
    def check_interactions_btn(self, locator: tuple):
        self.check_elm(locator)
        return self

    @allure.step("check book store btn")
    def check_book_store_btn(self, locator: tuple):
        self.check_elm(locator)
        return self

    @allure.step("check link")
    def check_link(self, locator: tuple):
        self.check_elm(locator)

#click
    @allure.step("click elements btn")
    def click_elements_btn(self):
        self.click_by_locator(self.elements_btn)
        return self

    @allure.step("click forms btn")
    def click_forms_btn(self):
        self.click_by_locator(self.forms_btn)
        return self

    @allure.step("click alerts btn")
    def click_alerts_btn(self):
        self.click_by_locator(self.alerts_btn)
        return self

    @allure.step("click widget btn")
    def click_widget_btn(self):
        self.click_by_locator(self.widget_btn)
        return self

    @allure.step("click interactions btn")
    def click_interactions_btn(self):
        self.click_by_locator(self.interactions_btn)
        return self

    @allure.step("click book store btn")
    def click_book_store_btn(self):
        self.click_by_locator(self.book_store_btn)
        return self
















