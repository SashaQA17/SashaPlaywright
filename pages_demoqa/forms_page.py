from pages_common.base_page import BasePage
import allure


class FormsPage(BasePage):

    url = 'https://demoqa.com/forms'

    def __init__(self, page):
        super().__init__(page)


#open
    @allure.step("open form page")
    def open(self):
        self.open_page(self.url)
        return self






