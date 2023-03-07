import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from main_page_locators import *
@pytest.fixture(scope="session")
def browser():
    options = Options()
    options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
    driver = webdriver.Firefox(executable_path=r'C:\WebDriver\bin\geckodriver.exe', options=options)  # Указываем с каким браузером работаем
    driver.maximize_window()  # Делаем полный экран
    yield driver  # Возвращаем генератор
    driver.quit()  # Выходим с браузера :)