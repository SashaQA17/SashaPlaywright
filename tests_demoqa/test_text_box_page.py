from pages_demoqa.main_page import MainPage
from pages_demoqa.text_box_page import TextBox
from pages_demoqa.left_menu_page import LeftMenuPage
from data.generate_person import generate
import allure
import pytest


@pytest.mark.skip_browser('firefox')
@allure.feature('text-box page')
@allure.story('check url')
def test_check_url(page):
    TextBox(page) \
        .open() \
        .check_url('https://demoqa.com/text-box') \
        #.screen_shot()

@pytest.mark.skip_browser('firefox')
@allure.feature('text-box page')
@allure.story('check the main text')
def test_main_text(page):
    TextBox(page) \
        .open() \
        .check_main_text()
        #.screen_shot()

@pytest.mark.skip_browser('firefox')
@allure.feature('text-box page')
@allure.story('check subtitle text')
def test_subtitle_text(page):
    TextBox(page) \
        .open() \
        .check_subtitle_text('Email') \
        .check_subtitle_text('Full Name') \
        .check_subtitle_text('Current Address') \
        .check_subtitle_text('Permanent Address') \

        #.screen_shot()

@pytest.mark.skip_browser('firefox')
@allure.feature('text-box page')
@allure.story('check name field')
def test_field_and_button(page):
    TextBox(page) \
        .open() \
        .check_field_and_btn('userName') \
        .check_field_and_btn('userEmail') \
        .check_field_and_btn('currentAddress') \
        .check_field_and_btn('permanentAddress') \
        .check_field_and_btn('submit')
        #.screen_shot()


@pytest.mark.skip_browser('firefox')
@allure.feature('text-box page')
@allure.story('fill in form')
def test_fill_in_form(page):
    TextBox(page) \
        .open() \
        .fill_in_form(generate().first_name, generate().email, generate().address, 'Grodno' ) \
        .screen_shot()


