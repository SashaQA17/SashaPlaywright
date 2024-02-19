from pages.main_page import MainPage
from pages.forms_page import FormsPage
import allure
import pytest


@allure.feature('main page')
@allure.story('check main page')
def test_p2p(page):
    MainPage(page) \
        .open() \
        .click_forms_btn()
    FormsPage(page) \
        .click_practice_form_btn()
