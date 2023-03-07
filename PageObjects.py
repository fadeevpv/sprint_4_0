from main_page_locators import *
from order_page_locators import *
from BasePage import BasePage
from selenium.webdriver.common.by import By

""""Создадим класс PagesLocators кторый будет использоваться для хранения локаторв"""


class PagesLocators:
    # блок блок локаторов для кнопок
    cookie_button = button_cookie  # кнопка cookie на гоавной странице
    first_question_button = first_question  # вопрос кнопка первая
    second_question_button = second_question  # вопрос кнопка вторая
    third_question_button = third_question  # вопрос кнопка третья
    fourth_question_button = fourth_question  # вопрос кнопка четвертая
    fifth_question_button = fifth_question  # вопрос кнопка пятая
    sixth_question_button = sixth_question  # вопрос кнопка шестая
    seventh_question_button = seventh_question  # вопрос кнопка седьмая
    eighth_question_button = eighth_question  # вопрос кнопка осьмая
    order_on_top_button = button1_get_order_on_top  # кнопка заказть в верху страницы
    order_on_down_button = button2_get_order_after_scrolling  # кнока заказть после несколкьих скролов в низ
    confirm_button = button_confirm_order  # кнопка  ДА для подтверждения заказа
    term_of_use_button = button_term_of_use  # кнопка выпадаюзего списка для выбора на какой срок нужен самокат
    order_status_button = button_status_of_order  # кнопка статус заказа
    next_button = button_next  # кнопка далее оформление заказа
    station_metro_button = metro_station_button  # кнопка выпадащего списка станция мтеро
    choice_station_button = choice_metro_station_button  # кнопка конкретной станции
    take_order_button = button_take_order  # кнопка заказать заказ после заполнения всех необходимых форм

    # блок локаторов для  форм ввода
    user_name = short_user_name  # поле ввода имени пользователя
    last_name = last_user_name  # поле ввода фамилия пользователя
    address_user = location_user  # поле ввода адрес пользователя
    phone_number = phone_user  # поле ввода номера телефона
    comment = comment_for_delivery  # поле ввода коментария для курьера
    date_form = delivery_date_order  # форма ввода для даты

    # блок локаторов для чек боксов, выбор дней в календаре итд
    scuter_collo = collor_scooter  # выбор цвета самоката
    data_delivery = day_delivery_order  # локатор дня доставки смоката у нас это 27
    header_logo_yandex_scooter = header_logo_yandex_scooter  # локатор логотипа Самокат
    logo_yandex = header_logo_yandex  # локатор логитипа Yandex
    question_heeader_main_page = header_questions  # заголовок блока вопросов
    text_arenda = arenda  # текст аренда на странице оформления заказа
    day_term_of_use = term_of_use  # сколько дней будет использоваться самокат  у нас 4 суток


"""Создадим класс Questions_Block, наследуем от класса BasePage из файла base_page"""


class Question_Block(BasePage):
    def check_first_question(self):
        self.driverwait(PagesLocators.cookie_button).click()  # кликаем по кнопке cookie чотбы скрыть блок про куки
        self.driverwait(PagesLocators.first_question_button).click()  # кликаем по кнопке первого вопроса

    def check_second_question(self):
        self.driverwait(PagesLocators.second_question_button).click()  # метод для клика по кнопке второго вопроса

    def check_third_question(self):
        self.driverwait(PagesLocators.third_question_button).click()  # метод для клика по кнопке третьего вопроса

    def check_fourth_question(self):
        self.driverwait(PagesLocators.fourth_question_button).click()  # метод для клика по кнопке четвертого вопроса

    def check_fifth_question(self):
        self.driverwait(PagesLocators.fifth_question_button).click()  # метод для клика по кнопке пятого вопроса

    def check_sixth_question(self):
        self.driverwait(PagesLocators.sixth_question_button).click()  # метод для клика по кнопке шестого вопроса

    def check_seventh_question(self):
        self.driverwait(PagesLocators.seventh_question_button).click()  # метод для клика по кнопке седьмого вопроса

    def check_eighth_question(self):
        self.driverwait(PagesLocators.eighth_question_button).click()  # метод для клика по кнопке восьмого вопроса


class Main_Page(BasePage):
    def click_to_order_top(self):
        self.driverwait(PagesLocators.order_on_top_button).click()  # кликаем по кнопке заказать вверхней части сайта

    def click_to_order_down(self):
        self.driverwait(
            PagesLocators.order_on_down_button).click()  # кликаем по кнопке заказать в нижней части сайта под блоком попросов

    """Создаем класс для  ORDER_PAGE заполнения форм зазака"""


class Order_Page(BasePage):
    # В fill_name заполняем имя и фамилию.
    def fill_name(self):

        self.driverwait(PagesLocators.user_name).send_keys('Кукумбер')
        self.driverwait(PagesLocators.last_name).send_keys('Огурцович')

    # В close_cookie закрываем куки
    def close_cookie(self):
        self.driverwait(PagesLocators.cookie_button).click()  # кликаем по кнопке cookie чотбы скрыть блок про куки

    # В fill_address заполняем адрес и метро.
    def fill_address(self):
        self.driverwait(PagesLocators.address_user).send_keys('Грядка номер 8, лумка 4 ')
        self.driverwait(PagesLocators.station_metro_button).click()
        self.driverwait(PagesLocators.choice_station_button).click()

    # В fill_phone заполняем номер телефона и нажимаем далее.
    def fill_phone(self):
        self.driverwait(PagesLocators.phone_number).send_keys('89612653265')
        self.driverwait(PagesLocators.next_button).click()

    def text_arenda(self):
        about_arenda = self.driverwait(PagesLocators.text_arenda)
        return about_arenda.text


""" Класс About_Rent для формы - Про Аренду """


class About_Rent(BasePage):
    # В fill_date заполняем дату.
    def fill_date(self):
        self.driverwait(PagesLocators.date_form).send_keys('27.03.2023')
        self.driverwait(PagesLocators.data_delivery).click()
        self.driverwait(PagesLocators.term_of_use_button).click()
        self.driverwait(PagesLocators.day_term_of_use).click()

    # В fill_other заполняем цвет, комментарий, и нажимаем кнопку заказать, подтверждаем заказ.
    def fill_other(self):
        self.driverwait(PagesLocators.scuter_collo).click()
        self.driverwait(PagesLocators.comment).send_keys('Привести к 18:00.')
        self.driverwait(PagesLocators.take_order_button).click()
        self.driverwait(PagesLocators.confirm_button).click()

    # В check_status нажимаем на кнопку "проверить статус".
    def check_status(self):
        self.driverwait(PagesLocators.order_status_button).click()

    def find_arenda_button(self):
        arenda_text = self.driverwait(PagesLocators.order_status_button)
        return arenda_text.text

    def check_up_buttom(self):
        up_buttom = self.driverwait(PagesLocators.order_on_top_button)
        return up_buttom.text

    def check_arenda_buttom(self):
        arenda_buttom = self.driverwait(PagesLocators.text_arenda)
        return arenda_buttom.text


""" Класс YandexButton создан для кнопок "Яндекс" и "Самокаты"."""


class YandexButton(BasePage):
    # В click_on_yandex_button мы нажимаем на кнопку "Яндекс".
    def click_on_yandex_button(self):
        self.driverwait(PagesLocators.logo_yandex).click()

    # В click_on_scooter_button мы нажимаем на кнопку "Самокаты".
    def click_on_scooter_button(self):
        self.driverwait(PagesLocators.header_logo_yandex_scooter).click()
