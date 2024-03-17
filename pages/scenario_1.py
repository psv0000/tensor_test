from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class SbisPageOne(BasePage):
    contacts = (By.PARTIAL_LINK_TEXT, 'Контакты')
    tensor_image = (
        By.XPATH,
        '//img[@alt="Разработчик системы СБИС — компания «Тензор»"]',
    )
    people_strength_block = (By.XPATH, '//p[contains(text(), "Сила в людях")]')

    def move_to_contacts(self):
        self.find_element(self.contacts).click()

    def move_to_tensor(self):
        self.find_element(self.tensor_image).click()
        self.switch_window(1)
        self.scroll_down(1750)

    def is_there_a_block(self):
        return self.find_element(self.people_strength_block).text


class TensorPage(BasePage):
    futher_navigation = (By.PARTIAL_LINK_TEXT, 'Подробнее')
    puctures = (By.XPATH, '//img[@loading="eager"]')

    def move_to_further(self):
        elements = self.find_elements(self.futher_navigation)
        self.scroll_down(1750)
        elements[2].click()

    def is_images_equal(self):
        self.scroll_down(1700)
        pictures = self.find_elements(self.puctures)
        height = all(
            map(
                lambda x: x == pictures[0].size['height'],
                map(lambda x: x.size['height'], pictures),
            )
        )
        width = all(
            map(
                lambda x: x == pictures[0].size['width'],
                map(lambda x: x.size['width'], pictures),
            )
        )
        return all((height, width))
