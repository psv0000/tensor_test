import time
from selenium.webdriver.common.by import By

from pages.scenario_1 import SbisPageOne


class SbisPageTwo(SbisPageOne):
    contacts = (By.PARTIAL_LINK_TEXT, 'Контакты')
    local_region = (By.XPATH, '//span[@tabindex="0"]')
    partners = (By.XPATH, '//div[@data-qa="item"]')
    region_41 = (By.XPATH, '//*[@title="Камчатский край"]')

    def get_local_region(self):
        return self.find_element(self.local_region).text

    def get_partners_quantity(self):
        return self.count_elements(self.partners)

    def get_partners_names(self):
        return self.get_elements_names(self.partners)

    def change_region(self, timeout=0.5):
        self.find_element(self.local_region).click()
        self.find_element(self.region_41).click()
        time.sleep(timeout)
