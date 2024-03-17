import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from pages.base_page import BasePage


class SbisPageThree(BasePage):
    download_local_versions = (By.LINK_TEXT, 'Скачать локальные версии')
    sbis_plugin = (By.XPATH, '//div[@data-id="plugin"]')
    web_installer = (By.PARTIAL_LINK_TEXT, "Скачать")

    def move_to_download_local_versions(self, timeout=1):
        element = self.find_element(self.download_local_versions)
        element.send_keys(Keys.PAGE_DOWN)
        element.click()
        time.sleep(timeout)

    def move_to_sbis_plugin(self, timeout=1):
        self.find_element(self.sbis_plugin).click()
        time.sleep(timeout)

    def get_web_installer(self):
        element = self.find_elements(self.web_installer)
        return element[0]

    def get_web_installer_url(self):
        return self.get_web_installer().get_attribute('href')

    def download_web_installer(self):
        element_url = self.get_web_installer_url()
        self.download_file(element_url)

    def check_downloaded_file(self):
        element_url = self.get_web_installer_url()
        return os.path.isfile(self.get_filename(element_url))

    def get_file_size_from_page(self):
        return float(self.get_web_installer().text.split()[2])

    def get_downloaded_file_size(self):
        element_url = self.get_web_installer_url()
        file_size_in_bytes = os.path.getsize(self.get_filename(element_url))
        file_size_in_mb = file_size_in_bytes / 1024**2
        return round(file_size_in_mb, 2)
