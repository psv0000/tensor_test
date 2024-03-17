import allure
from pages.scenario_3 import SbisPageThree
from confest import browser


@allure.feature('Check plugin downloaded')
def test_plugin_downloaded(browser):
    '''Проверка скачивания файла'''

    url = 'https://sbis.ru/'
    with allure.step(f'Выполняется переход на {url}'):
        sbis_page = SbisPageThree(browser, url)
    with allure.step(f'Выполняется переход в "Скачать локальные версии"'):
        sbis_page.move_to_download_local_versions()
    with allure.step(f'Выполняется переход в "СБИС Плагин"'):
        sbis_page.move_to_sbis_plugin()
    with allure.step(f'Скачивание Веб-Установщика'):
        sbis_page.download_web_installer()
    with allure.step(f'Проверка скачивания Веб-Установщика'):
        assert sbis_page.check_downloaded_file() == True


@allure.feature('Check plugin size')
def test_plugin_size(browser):
    '''Проверка размеров скаченного файла с указанным на сайте'''

    url = 'https://sbis.ru/download/'
    with allure.step(f'Выполняется переход на {url}'):
        sbis_page = SbisPageThree(browser, url)
    with allure.step(f'Выполняется переход в "СБИС Плагин"'):
        sbis_page.move_to_sbis_plugin()
    with allure.step(f'Проверка размеров скаченного файла с указанным на сайте'):
        assert (
            sbis_page.get_downloaded_file_size() == sbis_page.get_file_size_from_page()
        )
