from pages.base_page import BasePage
import allure


elements_btn = '//h5[text()="Elements"]'
forms_btn = '//h5[text()="Forms"]'
alerts_btn = '//h5[text()="Alerts, Frame & Windows"]'
widget_btn = '//h5[text()="Widgets"]'
interactions_btn = '//h5[text()="Interactions"]'
book_store_btn = '//h5[text()="Book Store Application"]'


class MainPage(BasePage):
    def __init__(self, page):
        super().__init__(page)


#open
    def open(self, url):
        with allure.step("open main page"):
            self.open_page(url)

    async def open2(self, url):
        await self.open_page2(url)


#check
    def check_elements_btn(self, locator: tuple):
        with allure.step("check elements btn"):
            self.check_elm(locator)

    def check_forms_btn(self, locator: tuple):
        with allure.step("check forms btn"):
            self.check_elm(locator)

    def check_alerts_btn(self, locator: tuple):
        with allure.step("check alerts btn"):
            self.check_elm(locator)

    def check_widget_btn(self, locator: tuple):
        with allure.step("check widget btn"):
            self.check_elm(locator)

    def check_interactions_btn(self, locator: tuple):
        with allure.step("check interactions btn"):
            self.check_elm(locator)

    def check_book_store_btn(self, locator: tuple):
        with allure.step("check book store btn"):
            self.check_elm(locator)


#click
    def click_elements_btn(self):
        with allure.step("click elements btn"):
            self.click_by_locator(elements_btn)

    def click_forms_btn(self):
        with allure.step("click forms btn"):
            self.click_by_locator(forms_btn)

    def click_alerts_btn(self):
        with allure.step("click alerts btn"):
            self.click_by_locator(alerts_btn)

    def click_widget_btn(self):
        with allure.step("click widget btn"):
            self.click_by_locator(widget_btn)

    def click_interactions_btn(self):
        with allure.step("click interactions btn"):
            self.click_by_locator(interactions_btn)

    def click_book_store_btn(self):
        with allure.step("click book store btn"):
            self.click_by_locator(book_store_btn)














