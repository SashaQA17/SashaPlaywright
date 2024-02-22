from pages.main_page import MainPage
from pages.forms_page import FormsPage
from pages.base_page import BasePage
from pages.left_menu_page import LeftMenuPage
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


@pytest.mark.skip_browser('firefox')
@allure.feature('forms page')
@allure.story('check element list in the "Book store Application btn"')
def test_check_element_list(page):
    FormsPage(page) \
        .open()
    LeftMenuPage(page) \
        .click_book_store_application_btn() \
        .check_login_btn('//*[text() = "Login"]') \
        .check_book_store_btn('//*[text() = "Book Store"]') \
        .check_profile_btn('//*[text() = "Profile"]') \
        .check_book_store_api_btn('//*[text() = "Book Store API"]') \
        #.screen_shot()



