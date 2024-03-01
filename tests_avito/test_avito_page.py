from pages_avito.avito_start_page import AvitoStartPage
import allure
import pytest

@allure.feature('avito page')
@allure.story('p2p - fiend printers')
def testp2p_fiend_printers(page):
    AvitoStartPage(page) \
        .open() \
        .select_market_sub_category('Электроника', 'Оргтехника и расходники') \
        .fill_in_search_field('Принтер') \
        .select_region('Владивосток') \
        .sort_by('Дороже') \
        .print_text(5)




