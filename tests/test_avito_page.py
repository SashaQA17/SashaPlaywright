from pages.avito_start_page import AvitoStartPage
from pages.avito_orgtehnika_page import AvitoOrgtehnika
import allure
import pytest

@allure.feature('avito page')
@allure.story('p2p - fiend printers')
def testp2p_fiend_printers(page):
    AvitoStartPage(page) \
        .open() \
        .click_all_category_btn() \
        .click_electronika_btn() \
        .click_org_and_rash_btn()
    AvitoOrgtehnika(page) \
        .fill_in_search_field('Принтер') \
        .click_select_region() \
        .fill_in_region_field('Владивосток') \
        .select_first_item() \
        .click_show_result() \
        .click_sort_btn() \
        .click_expensive_btn() \
        .print_text()



