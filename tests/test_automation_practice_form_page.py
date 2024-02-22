from pages.main_page import MainPage
from pages.left_menu_page import LeftMenuPage
from pages.automation_practice_form_page import AutomationPracticeFormPage
from data.generate_person import generate
import allure
import pytest

male = '//*[contains(text(), "Male")]'
female = '//*[contains(text(), "Female")]'
other = '//*[contains(text(), "Other")]'

@allure.feature('automation practice form page')
@allure.story('check main text')
def test_check_main_text(page):
    AutomationPracticeFormPage(page) \
        .open() \
        .check_main_text('//h1[@class="text-center"]')\
        #.screen_shot()

@allure.feature('automation practice form page')
@allure.story('p2p test - check Student Registration Form')
@pytest.mark.parametrize("gender",[male, female, other])
def test_p2p(page, gender):
    MainPage(page) \
        .open() \
        .click_forms_btn()
    LeftMenuPage(page) \
        .click_practice_form_btn()
    AutomationPracticeFormPage(page) \
        .fill_in_first_name(generate().first_name) \
        .fill_in_last_name(generate().last_name) \
        .fill_in_email(generate().email) \
        .select_gender(gender) \
        #.screen_shot()






