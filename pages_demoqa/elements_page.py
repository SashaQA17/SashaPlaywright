from pages_common.base_page import BasePage


class ElementsPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

    def check_main_text(self, locator):
        self.check_elm(locator)
