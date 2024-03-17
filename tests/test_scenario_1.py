import allure
from pages.scenario_1 import SbisPageOne, TensorPage
from confest import browser


@allure.feature('Check the block')
def test_is_there_a_block(browser):
    '''Проверка есть ли блок "Сила в людях"'''

    url = 'https://sbis.ru/'
    with allure.step(f'Выполняется переход на {url}'):
        sbis_page = SbisPageOne(browser, url)
    with allure.step('Выполняется переход в раздел "Контакты"'):
        sbis_page.move_to_contacts()
    with allure.step('Выполняется переход на вкладку с https://tensor.ru/'):
        sbis_page.move_to_tensor()
    with allure.step('Выполняется проверка наличия блока "Сила в людях" на странице'):
        assert sbis_page.is_there_a_block() == 'Сила в людях'


@allure.feature('Check the url')
def test_check_url(browser):
    '''Проверка совпадения url адреса с "https://tensor.ru/about"'''

    url = 'https://tensor.ru/'
    with allure.step(f'Выполняется переход на {url}'):
        tensor_page = TensorPage(browser, url)
    with allure.step('Выполняется переход в "Подробнее" в блоке "Сила в людях"'):
        tensor_page.move_to_further()
    with allure.step('Выполняется проверка совпадения url адресов'):
        assert tensor_page.get_current_url() == 'https://tensor.ru/about'


@allure.feature('Check images size')
def test_check_images_size(browser):
    '''Проверка совпадения размеров у 4х фотографий хронологии'''

    url = 'https://tensor.ru/about/'
    with allure.step(f'Выполняется переход на {url}'):
        tensor_page = TensorPage(browser, url)
    with allure.step(
        'Выполняется проверка совпадения размеров у 4х фотографий хронологии'
    ):
        assert tensor_page.is_images_equal() == True
