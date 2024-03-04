from pages_common.base_page import BasePage
from playwright.sync_api import expect
import allure


class AvitoStartPage(BasePage):

    url = 'https://www.avito.ru/penza/transport?cd=1'
    new_btn = '//span[text()="Новые"]'
    fiend_btn = '//span[text()="Найти"]'
    all_category_btn ='//button[@data-marker="top-rubricator/all-categories"]'
    region_btn = '//div[@data-marker="search-form/change-location"]'
    search_field = '//input[@data-marker ="search-form/suggest"]'
    region_field = '//input[@placeholder = "Город или регион"]'
    first_item = '//ul[@data-marker="suggest-list"]/li[1]//strong'
    show_result_btn = '//button[@type="button"]/span[contains(text(), "Показать")]'
    sort_btn = '//*[@id="app"]//div[1]/div[2]/div/span[text()="Сортировка"]'
    price = '//strong[@class="styles-module-root-LIAav"]/span'
    first_price = '//div[@data-marker="item"][1]//strong/span'
    second_price = '//div[@data-marker="item"][2]//strong/span'

    def __init__(self, page):
        super().__init__(page)

#open
    def open(self):
        with allure.step("open first link"):
            self.open_page(self.url)
            return self

#click
    def click_new_btn(self):
        with allure.step("click new btn"):
            self.check_checkbox(self.new_btn)
            return self

    def click_fiend(self):
        with allure.step("click fiend brtn"):
            self.click_by_locator(self.fiend_btn)
            return self

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

    def select_sort(self, param):
        with allure.step(f"select sort by {param} "):
            self.click_by_locator(f'//div[text()="{param}"]')
            return self

#fill_in
    def fill_in_search_field(self, text: str):
        with allure.step("fill in search field"):
            self.page.wait_for_selector('//*[@*="Поиск по объявлениям"]').is_disabled()
            self.fill_in_by_locator(self.search_field, text)
            self.page.wait_for_timeout(1000)
            self.click_fiend()
            self.page.wait_for_timeout(1000)
            self.click_new_btn()
            self.page.wait_for_timeout(1000)
            return self

    def fill_in_region_field(self, text: str):
        with allure.step(f"fill in search field: {text}"):
            self.clear_and_fill_in(self.region_field, text)
            return self

#functional
    def select_region(self, region: str):
        with allure.step(f"select region: {region}"):
            self.click_select_region()
            self.page.wait_for_timeout(1000)
            self.fill_in_region_field(region)
            self.page.wait_for_timeout(1000)
            self.select_first_item()
            self.click_show_result()
            return self

    def sort_by(self, param: str):
        with allure.step(f"sort by {param}"):
            self.page.wait_for_timeout(1000)
            self.click_sort_btn()
            self.page.wait_for_timeout(1000)
            self.select_sort(param)
            self.page.wait_for_timeout(3000)
            return self

    def print_text(self, count):
        with  allure.step(f"print the first {count} prices"):
            elements = self.page.query_selector_all('//p[@data-marker="item-price"]/strong/span')
            prices = elements[0:min(count, len(elements))]
            for i in prices:
                print(i.text_content())
                return self


    def select_market_sub_category(self, category, subcategory):
        with allure.step("click all category btn"):
            self.click_by_locator(self.all_category_btn)

        with allure.step(f"click {category} btn"):
            self.click_by_locator(f'//p[text()="{category}"]')

        if subcategory is not None:
            with allure.step("click orgtehnika and rashodniki btn"):
                self.click_by_locator(f'//strong[@data-name="{subcategory}"]')
        return self







