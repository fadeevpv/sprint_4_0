import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from PageObjects import Question_Block, Main_Page, Order_Page, About_Rent, YandexButton, PagesLocators


class TestOrders:
    """Создаем тестовый класс и методы"""

    @allure.title('Тест кнопки заказать')
    @allure.feature('Test button')
    @allure.story('Проверяем кнопку заказать')
    def test_click_button_top(self, browser):
        first_question = Question_Block(browser)
        first_question.go_to_site()
        main = Main_Page(browser)
        browser.refresh()
        main.click_to_order_top()

    @allure.title('Закрываем Куки')
    @allure.feature('Close cookie')
    @allure.story('Кликаем по кнопке чтобы закрыть куки')
    def test_close_cookie(self, browser):
        close = Order_Page(browser)
        close.close_cookie()

    @allure.title('Заполнение имени')
    @allure.feature('Filling out name')
    @allure.story('Заполняем имя и фамилию')
    def test_fill_out_name(self, browser):
        write_in_name = Order_Page(browser)
        write_in_name.fill_name()

    @allure.title('Заполнение адреса')
    @allure.feature('Filling out address')
    @allure.story('Заполняем адрес')
    def test_fill_out_address(self, browser):
        write_in_address = Order_Page(browser)
        write_in_address.fill_address()

    @allure.title('Заполнение телефона')
    @allure.feature('Filling out phone number')
    @allure.story('Заполняем номер телефона')
    def test_fill_out_phone(self, browser):
        write_in_phone = Order_Page(browser)
        write_in_phone.fill_phone()


    @allure.title('Проверка заполнения данных')
    @allure.feature('Checking the filling of data')
    @allure.story('Проверяем, что заполнили данные')
    def test_check_order(self, browser):
        check_order = About_Rent(browser)
        assert check_order.check_arenda_buttom() == "Про аренду"

    @allure.title('Заполнение "про аренду"')
    @allure.feature('Fill "about rent"')
    @allure.story('Заполняем "про аренду"')
    def test_fill_rent(self, browser):
        write_in_rent = About_Rent(browser)
        write_in_rent.fill_date()
        write_in_rent.fill_other()

    @allure.title('Проверка оформления заказа(верхняя кнопка)')
    @allure.feature('Fill "for rent"(top button)')
    @allure.story('Проверяем оформление заказа(верхняя кнопка)')
    def test_check_exe_of_the_order(self, browser):
        check = About_Rent(browser)
        assert check.check_up_buttom() == "Заказать"
        check.check_status()

    @allure.title('Проверка кнопок Яндекса')
    @allure.feature('Check Yandex buttons')
    @allure.story('Проверяем кнопки Яндекса"')
    def test_yandex_buttons(self, browser):
        click = YandexButton(browser)
        click.click_on_scooter_button()
        url = browser.current_url
        assert url == 'https://qa-scooter.praktikum-services.ru/'
        click.click_on_yandex_button()
        browser.switch_to.window(browser.window_handles[1])
        WebDriverWait(browser, 15).until(ec.url_changes("about:blank"))
        url = browser.current_url
        browser.close()
        assert url != 'https://yandex.ru/'
        browser.switch_to.window(browser.window_handles[0])

    @allure.title('Проверка кнопки заказа(нижняя)')
    @allure.feature('Check button(down)')
    @allure.story('Проверяем кнопку заказ(нижняя)"')
    def test_order_form_down(self, browser):
        order_form = Main_Page(browser)
        # element = PagesLocators.order_on_down_button
        # browser.execute_script("arguments[0].scrollIntoView();", element)
        order_form.click_to_order_down()
        fill_form = Order_Page(browser)
        fill_form.fill_name()
        fill_form.fill_address()
        fill_form.fill_phone()
        assert fill_form.text_arenda() == "Про аренду"

    @allure.title('Проверка оформления заказа(нижняя кнопка) ')
    @allure.feature('Fill "for rent"(down)')
    @allure.story('Проверяем оформление заказа(нижняя кнопка)"')
    def test_about_rent_down(self, browser):
        write_in_rent = About_Rent(browser)
        write_in_rent.fill_date()
        write_in_rent.fill_other()
        check = About_Rent(browser)
        check.find_arenda_button()
        assert check.find_arenda_button() == "Посмотреть статус"
        check.check_status()
