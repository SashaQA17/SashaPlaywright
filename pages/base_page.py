from playwright.sync_api import Page, expect
from datetime import datetime

class BasePage:
    def __init__(self, page: Page):
        self.page = page

#open
    def open_page(self, url):
        self.page.goto(url)

    async def open_page2(self, url):
        await self.page.goto(url)


#fiend
    def fiend_by_locator(self, locator: tuple):
        self.page.locator(locator)


#click
    def click_by_locator(self, locator: tuple):
        self.page.locator(locator).click()

    def click_by_text(self, text):
        self.page.get_by_text(text).click()


#fill_in
    def fill_in_by_locator(self, locator: tuple):
        self.page.locator().fill()


#check
    def check_elm(self, locator: tuple):
        element = self.page.locator(locator)
        expect(element).to_be_visible()

    def check_text(self, text: str):
        element = self.page.get_by_text(text)
        expect(element).to_be_visible()


#screenshot
    def screen_shot(self):
        current_time = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        screen = f"screenshot_{current_time}.png"
        self.page.screenshot(path=f'/Users/sasha/PycharmProjects/SashaPlaywright/screenshots/{screen}')
















