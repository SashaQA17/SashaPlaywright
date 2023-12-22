from pages.base_page import BasePage


practice_form_btn = 'Practice Form'


class FormsPage(BasePage):
    def __init__(self, page):
        super().__init__(page)


    def click_practice_form_btn(self):
        self.click_by_text(practice_form_btn)

