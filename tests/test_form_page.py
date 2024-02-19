from pages.main_page import MainPage
from pages.forms_page import FormsPage
from pages.base_page import BasePage
import allure
import pytest


@pytest.mark.skip_browser('firefox')
@allure.feature('forms page')
@allure.story('check title')
def test_title(page):
    FormsPage(page) \
        .open() \
        .check_url('https://demoqa.com/forms') \
        #.screen_shot()

@pytest.mark.skip_browser('firefox')
@allure.feature('forms page')
@allure.story('check practice form btn')
def test_check_practice_form_btn(page):
    FormsPage(page) \
        .open() \
        .check_practice_form_btn('//span[text()="Practice Form"]') \
        #.screen_shot()

@pytest.mark.skip_browser('firefox')
@allure.feature('forms page')
@allure.story('click practice form btn')
def test_click_practice_form_btn(page):
    FormsPage(page) \
        .open() \
        .click_practice_form_btn() \
        .check_url('https://demoqa.com/automation-practice-form')
        #.screen_shot()
