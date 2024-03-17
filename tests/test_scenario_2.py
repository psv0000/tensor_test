import allure
from pages.scenario_2 import SbisPageTwo
from confest import browser


@allure.feature('Check the local region')
def test_local_region(browser):
    '''Проверка отображения местного региона'''

    url = 'https://sbis.ru/'
    with allure.step(f'Выполняется переход на {url}'):
        sbis_page = SbisPageTwo(browser, url)
    with allure.step('Выполняется переход в раздел "Контакты"'):
        sbis_page.move_to_contacts()
    assert sbis_page.get_local_region() == 'Свердловская обл.'


@allure.feature('Check partners existence')
def test_is_there_partners(browser):
    '''Проверка наличия партнеров'''

    url = 'https://sbis.ru/contacts/'
    with allure.step(f'Выполняется переход на {url}'):
        sbis_page = SbisPageTwo(browser, url)
    with allure.step('Выполняется проверка наличия партнеров'):
        assert sbis_page.get_partners_quantity() > 0


@allure.feature('Check title, url, partners change')
def test_title(browser):
    '''
    Проверка изменения региона в названии вкладки, 
    и в адресной строке, также проверка изменения списка партнеров
    '''

    errors = []
    url = 'https://sbis.ru/contacts/'
    with allure.step(f'Выполняется переход на {url}'):
        sbis_page = SbisPageTwo(browser, url)
    local_partners = sbis_page.get_partners_names()
    with allure.step('Выполняется смена региона на "41 Камчатский край"'):
        sbis_page.change_region()
    with allure.step('Выполняется проверка изменения региона в названии вкладки'):
        if not sbis_page.get_current_title() == 'СБИС Контакты — Камчатский край':
            errors.append('Не прошла проверка изменения региона в названии вкладки')
    with allure.step('Выполняется проверка изменения региона в адресной строке'):
        if not '41-kamchatskij-kraj' in sbis_page.get_current_url():
            errors.append('Не прошла проверка изменения региона в адресной строке')
    region41_partners = sbis_page.get_partners_names()
    with allure.step('Выполняется проверка изменения списка партнеров'):
        if not local_partners != region41_partners:
            errors.append('Не прошла проверка изменения списка партнеров')
    assert not errors, f'{', '.join(errors)}'
