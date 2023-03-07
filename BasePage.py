from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from main_page_locators import *


class BasePage:  # Оперделяем базовыы метоы для работы с драйвером

    def __init__(self, driver):
        self.driver = driver
        self.base_url = main_page  # ссылка на главную страницу
        self.quantity = 0  # будем испольовать для открытия страницы .

    def driverwait(self, locator):
        return WebDriverWait(self.driver, 20).until(ec.visibility_of_element_located(locator))    # ожидаем загрузку страницы


    def go_to_site(self):
        return self.driver.get(self.base_url)    # Вызываем функцию, для перехода на главную страницу.