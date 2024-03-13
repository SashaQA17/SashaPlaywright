from pages_common.base_page import BasePage
import allure


class AvitoStartPage(BasePage):

    url = 'https://www.avito.ru/penza/transport?cd=1'
    new_btn = '//span[text()="Новые"]'
    find_btn = '//span[text()="Найти"]'
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
    @allure.step("open first link")
    def open(self):
        self.page.set_default_timeout(60000)
        self.open_page(self.url)
        return self

#click
    @allure.step("click find btn")
    def click_find(self):
        self.click_by_locator(self.find_btn)
        return self

    @allure.step("click select region btn")
    def click_select_region(self):
        self.click_by_locator(self.region_btn)
        return self

    @allure.step("select first item")
    def select_first_item(self):
        self.click_by_locator(self.first_item)
        return self

    @allure.step("click show result btn")
    def click_show_result(self):
        self.click_by_locator(self.show_result_btn)
        return self

    @allure.step("click sort btn")
    def click_sort_btn(self):
        self.click_by_locator(self.sort_btn)
        return self

    @allure.step("select sort by {param}")
    def select_sort(self, param):
        self.click_by_locator(f'//div[text()="{param}"]')
        return self

#check
    @allure.step("set new checkbox as: {state}")
    def check_new_checkbox(self, state):
        self.check_checkbox(self.new_btn, state)
        return self


#fill_in
    @allure.step("fill in search field: {text}")
    def fill_in_region_field(self, text: str):
        self.clear_and_fill_in(self.region_field, text)
        return self

#functional
    @allure.step("fill in search field")
    def fill_in_search_field(self, text: str):
        self.page.wait_for_selector('//*[@*="Поиск по объявлениям"]').is_visible()  # Ждем пока в поле появиться текс
        el = self.page.locator(self.search_field)  # Находим поисковое поле, кликаем, вводим текст
        el.click()
        el.type(text)
        self.click_find() # Нажимаем кнопку найти значение из поискового поля
        self.page.wait_for_load_state()
        return self

    @allure.step("select region: {region}")
    def select_region(self, region: str):
        self.click_select_region()  # Нажать на выбор региона
        self.fill_in_region_field(region)  # В окне выбора региона ввести значение в поле
        self.select_first_item()  # Выбрать первый элемент из списка автодополнения
        self.click_show_result()  # Нажать на кнопку Показать результаты, внутри проверятся что она загрузилась
        self.page.wait_for_load_state()
        return self

    @allure.step("sort by {param}")
    def sort_by(self, param: str):
        self.click_sort_btn() # Нажимаем на сортировку вывода поиска
        self.select_sort(param) # Выбираем пораметр сортировки
        self.page.wait_for_load_state()
        return self

    @allure.step("print the first {count} prices")
    def print_text(self, count):
        elements = self.page.query_selector_all('//p[@data-marker="item-price"]/strong/span')  # Выводим цену товара
        prices = elements[0:min(count, len(elements))]
        print()
        for i in prices:
            print(i.text_content())
        return self

    @allure.step("select sub_category")
    def select_market_sub_category(self, category, subcategory):
        with allure.step("click all category btn"):
            self.click_by_locator(self.all_category_btn)  # Нажимаем на кнопку: все категории

        with allure.step(f"click category: {category}"):
            self.click_by_locator(f'//p[text()="{category}"]') # Выбираем одну из каткгорий

        if subcategory is not None:
            with allure.step(f"click subcategory: {subcategory}"): # Выбираем одну из подкатегорий
                self.click_by_locator(f'//strong[@data-name="{subcategory}"]')
        return self




