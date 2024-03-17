import requests
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.get_url(url)

    def get_url(self, url):
        self.driver.get(url)
        self.driver.maximize_window()

    def scroll_down(self, offset=500):
        ActionChains(self.driver).scroll_by_amount(0, offset).perform()

    def scroll_up(self, offset=500):
        ActionChains(self.driver).scroll_by_amount(0, -offset).perform()

    def get_browser_windows(self):
        return self.driver.window_handles

    def switch_window(self, value):
        browser_windows = self.get_browser_windows()
        if -1 < value <= len(browser_windows):
            self.driver.switch_to.window(browser_windows[value])
        else:
            raise ValueError(
                f'Значение {value} больше количества вкладок на странице {len(browser_windows)}'
            )

    def get_current_title(self):
        return self.driver.title

    def get_current_url(self):
        return self.driver.current_url

    def find_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator),
            message=f"Элемент с локатором {locator} не найден",
        )

    def find_elements(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_all_elements_located(locator),
            message=f"Элементы с локатором {locator} не найдены",
        )

    def get_elements_names(self, locator):
        elements = self.find_elements(locator)
        return set(map(lambda x: x.text, elements))

    def count_elements(self, locator):
        return len(self.find_elements(locator))

    def get_filename(self, url):
        return url[url.rfind('/') + 1 :]

    def download_file(self, url):
        req = requests.get(url)
        filename = self.get_filename(url)
        if req.status_code == 200:
            with open(filename, 'wb') as f:
                for chunk in req:
                    f.write(chunk)
