from playwright.sync_api import Page, expect
from datetime import datetime
import allure


class BasePage:
    def __init__(self, page: Page):
        self.page = page

#open
    def open_page(self, url):
        self.page.goto(url)

    async def open_page_async(self, url):
        await self.page.goto(url)

#fiend
    def fiend_by_locator(self, locator: tuple):
        self.page.locator(locator)

#click
    def click_by_locator(self, locator: tuple):
        self.page.locator(locator).click()

    def check_checkbox(self, locator: tuple):
        self.page.locator(locator).check()
        self.page.wait_for_selector(locator).is_checked()

    def click_by_text(self, text: str):
        self.page.get_by_text(text).click()

#fill_in
    def fill_in_by_locator(self, locator: tuple, text: str):
        self.page.locator(locator).fill(text)

    def clear_and_fill_in(self, locator: tuple, text: str):
        self.page.locator(locator).clear()
        self.page.locator(locator).fill(text)

#check
    def check_url(self, url):
        with allure.step("check url"):
            expect(self.page).to_have_url(url)
            return self

    def check_title(self, text: str):
        with allure.step("check title"):
            expect(self.page).to_have_title(text)
            return self

    def check_elm(self, locator: tuple):
        element = self.page.locator(locator)
        expect(element).to_be_visible()

    def check_text(self, text: str):
        element = self.page.get_by_text(text)
        expect(element).to_be_visible()

#get text
    def get_text(self, locator):
        return self.page.locator(locator).text_content()



#screenshot
    def screen_shot(self):
        current_time = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        screen = f"screenshot_{current_time}.png"
        self.page.screenshot(path=f'/Users/sasha/PycharmProjects/SashaPlaywright/screenshots/{screen}')
        return self



    # def print_text(self, locator):
    #         price = self.page.query_selector(locator)
    #         print(price.text_text())















