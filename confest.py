import pytest
from selenium import webdriver


@pytest.fixture()
def browser():
    options = webdriver.ChromeOptions()
    options.add_experimental_option('detach', True)
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()
