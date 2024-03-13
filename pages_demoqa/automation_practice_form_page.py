from pages_common.base_page import BasePage
import allure


class AutomationPracticeFormPage(BasePage):

    url = 'https://demoqa.com/automation-practice-form'
    practice_form = '//h1[@class="text-center"]'
    first_name = '//input[@id="firstName"]'
    last_name = '//input[@id="lastName"]'
    email = '//input[@id="userEmail"]'
    male = '//*[contains(text(), "Male")]'

    def __init__(self, page):
        super().__init__(page)


#open
    @allure.step("open automation practice form page")
    def open(self):
        self.open_page(self.url)
        return self

#check
    @allure.step("check text")
    def check_main_text(self, locator: tuple):
        self.check_elm(locator)
        return self

#click
    @allure.step("select gender")
    def select_gender(self, locator: tuple):
        self.click_by_locator(locator)
        return self

#fill_in
    @allure.step("fill in first name")
    def fill_in_first_name(self, text: str):
        self.fill_in_by_locator(self.first_name, text)
        return self

    @allure.step("fill in last name")
    def fill_in_last_name(self, text: str):
        self.fill_in_by_locator(self.last_name, text)
        return self

    @allure.step("fill in email")
    def fill_in_email(self, text: str):
        self.fill_in_by_locator(self.email, text)
        return self

