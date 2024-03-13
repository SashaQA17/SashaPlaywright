import allure
import pytest

from pages_avito.avito_start_page import AvitoStartPage


@allure.feature('avito page')
@allure.story('p2p - find printers')
def testp2p_find_printers(page):
    AvitoStartPage(page) \
        .open() \
        .select_market_sub_category('Электроника', 'Оргтехника и расходники')
        # .fill_in_search_field('Принтер') \
        # .check_new_checkbox('Да') \
        # .select_region('Владивосток') \
        # .sort_by('Дороже') \
        # .print_text(5)


@allure.feature('avito page')
@allure.story('p2p - find printers 2')
def testp2p_find_printers2(page):
    AvitoStartPage(page) \
        .open() \
        .select_market_sub_category('Электроника', 'Оргтехника и расходники')