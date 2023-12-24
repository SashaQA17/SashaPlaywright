from pages.main_page import MainPage
from pages.forms_page import FormsPage
from pages.elements_page import ElementsPage
from playwright.sync_api import expect
import pytest
import allure

@pytest.mark.skip_browser('firefox')
@allure.feature('main page')
@allure.story('check main page')
def test_title(page):
    main_page = MainPage(page)
    main_page.open('https://demoqa.com/')
    expect(page).to_have_title('DEMOQA')
    #main_page.screen_shot()

@pytest.mark.only_browser('chromium')
@allure.feature('main page')
@allure.story('check all buttons')
def test_all_buttons(page):
    main_page = MainPage(page)
    main_page.open('https://demoqa.com/')
    main_page.check_elements_btn('//h5[text()="Elements"]')
    main_page.check_forms_btn('//h5[text()="Forms"]')
    main_page.check_alerts_btn('//h5[text()="Alerts, Frame & Windows"]')
    main_page.check_widget_btn('//h5[text()="Widgets"]')
    main_page.check_interactions_btn('//h5[text()="Interactions"]')
    main_page.check_book_store_btn('//h5[text()="Book Store Application"]')
    #main_page.screen_shot()

@pytest.mark.only_browser('chromium')
@allure.feature('main page')
@allure.story('check elements btn')
def test_elements_btn(page):
    main_page = MainPage(page)
    main_page.open('https://demoqa.com/')
    main_page.click_elements_btn()
    expect(page).to_have_url('https://demoqa.com/elements')
    #main_page.screen_shot()

@pytest.mark.skip_browser('chromium')
@allure.feature('main page')
@allure.story('check forms btn')
def test_forms_btn(page):
    main_page = MainPage(page)
    main_page.open('https://demoqa.com/')
    main_page.click_forms_btn()
    expect(page).to_have_url('https://demoqa.com/forms')
    #main_page.screen_shot()

@pytest.mark.skip
@allure.feature('main page')
@allure.story('check alerts btn')
def test_alerts_btn(page):
    main_page = MainPage(page)
    main_page.open('https://demoqa.com/')
    main_page.click_alerts_btn()
    expect(page).to_have_url('https://demoqa.com/alertsWindows')
    #main_page.screen_shot()

@pytest.mark.skip
@allure.feature('main page')
@allure.story('check wiget btn')
def test_widget_btn(page):
    main_page = MainPage(page)
    main_page.open('https://demoqa.com/')
    main_page.click_widget_btn()
    expect(page).to_have_url('https://demoqa.com/widgets')
    #main_page.screen_shot()

@pytest.mark.skip_browser('chromium')
@allure.feature('main page')
@allure.story('check interactions btn')
def test_interactions_btn(page):
    main_page = MainPage(page)
    main_page.open('https://demoqa.com/')
    main_page.click_interactions_btn()
    expect(page).to_have_url('https://demoqa.com/interaction')
    #main_page.screen_shot()
v
@pytest.mark.only_browser('firefox')
@allure.feature('main page')
@allure.story('check booke store btn')
def test_book_store_btn(page):
    main_page = MainPage(page)
    main_page.open('https://demoqa.com/')
    main_page.click_book_store_btn()
    expect(page).to_have_url('https://demoqa.com/books')
    #main_page.screen_shot()









