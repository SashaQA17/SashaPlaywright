from pages_demoqa.main_page import MainPage
import allure
import pytest


@pytest.mark.skip_browser('firefox')
@allure.feature('main page')
@allure.story('check main page')
def test_title(page):
    MainPage(page) \
        .open() \
        .check_title('DEMOQA')\
        #.screen_shot()


@pytest.mark.only_browser('chromium')
@allure.feature('main page')
@allure.story('check all buttons')
def test_all_buttons(page):
    MainPage(page) \
        .open() \
        .check_elements_btn('//h5[text()="Elements"]') \
        .check_forms_btn('//h5[text()="Forms"]') \
        .check_alerts_btn('//h5[text()="Alerts, Frame & Windows"]') \
        .check_widget_btn('//h5[text()="Widgets"]') \
        .check_interactions_btn('//h5[text()="Interactions"]') \
        .check_book_store_btn('//h5[text()="Book Store Application"]') \
        #.screen_shot()


@pytest.mark.only_browser('chromium')
@allure.feature('main page')
@allure.story('check elements btn')
def test_elements_btn(page):
    MainPage(page) \
        .open() \
        .click_elements_btn() \
        .check_url('https://demoqa.com/elements') \
        #.screen_shot()


@pytest.mark.only_browser('chromium')
@allure.feature('main page')
@allure.story('check forms btn')
def test_forms_btn(page):
    MainPage(page) \
        .open() \
        .click_forms_btn() \
        .check_url('https://demoqa.com/forms') \
        #.screen_shot()


@pytest.mark.skip
@allure.feature('main page')
@allure.story('check alerts btn')
def test_alerts_btn(page):
    MainPage(page) \
        .open() \
        .click_alerts_btn() \
        .check_url('https://demoqa.com/alertsWindows') \
        #.screen_shot()


@pytest.mark.skip
@allure.feature('main page')
@allure.story('check wiget btn')
def test_widget_btn(page):
    MainPage(page) \
        .open() \
        .click_widget_btn() \
        .check_url('https://demoqa.com/widgets') \
        #.screen_shot()


@pytest.mark.skip_browser('chromium')
@allure.feature('main page')
@allure.story('check interactions btn')
def test_interactions_btn(page):
    MainPage(page) \
        .open() \
        .click_interactions_btn() \
        .check_url('https://demoqa.com/interaction') \
        #.screen_shot()


@pytest.mark.only_browser('firefox')
@allure.feature('main page')
@allure.story('check booke store btn')
def test_book_store_btn(page):
    MainPage(page) \
        .open() \
        .click_book_store_btn() \
        .check_url('https://demoqa.com/books') \
        #.screen_shot()









