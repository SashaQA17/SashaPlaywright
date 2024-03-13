from pages_avito.avito_start_page import AvitoStartPage
import allure
import pytest


@allure.feature('avito page2')
@allure.story('p2p - find printers21')
def testp2p_find_printers21(page):
    AvitoStartPage(page) \
        .open() \
        .select_market_sub_category('Электроника', 'Оргтехника и расходники')


@allure.feature('avito page2')
@allure.story('p2p - find printers 22')
def testp2p_find_printers22(page):
    AvitoStartPage(page) \
        .open() \
        .select_market_sub_category('Электроника', 'Оргтехника и расходники')