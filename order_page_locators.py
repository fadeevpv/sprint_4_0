from selenium.webdriver.common.by import By

# локаторы для форм оформления заказа
short_user_name = [By.XPATH, '//input[@placeholder="* Имя"]']     # локатор поля  ввода Имени
last_user_name = [By.XPATH, '//input[@placeholder="* Фамилия"]']  # локатор поля  ввода Фамилии
location_user = [By.XPATH, '//input[@placeholder="* Адрес: куда привезти заказ"]']  # локатор поля  ввода Адреса
phone_user = [By.XPATH, '//input[@placeholder="* Телефон: на него позвонит курьер"]']  # локатор поля  ввода телефона
metro_station_button = [By.XPATH, '//input[@class="select-search__input"]']  # локатор выподающего списка с выбором метро
choice_metro_station_button = [By.XPATH, '//button[@value="1"]']   # локатор выбираемой станции метро можно  добавить рандом
button_status_of_order = [By.XPATH, '/html/body/div/div/div[2]/div[5]/div[2]/button']  # локатор для кнопки статус заказа
button_next = [By.XPATH, '//button[@class="Button_Button__ra12g Button_Middle__1CSJM"]'] # локатор кнопки далее
header_logo_yandex_scooter = [By.XPATH, '//a[@class="Header_LogoScooter__3lsAR"]'] # локатор логотипа Яндекс Самокат для перехода на главную страницу
header_logo_yandex = [By.XPATH, '//a[@class="Header_LogoYandex__3TSOI"]'] # ЛОкатор для лого яндекс для прехода на страницу яндекса
delivery_date_order = [By.XPATH, '//input[@placeholder="* Когда привезти самокат"]']  # локтаор для формы выбора даты доставки товара
day_delivery_order = [By.XPATH, '//div[@class="react-datepicker__day react-datepicker__day--027 react-datepicker__day--selected"]'] # локатор для выбора дня даты доставки можно рандом использовать
button_term_of_use = [By.XPATH, '//div[@class="Dropdown-placeholder"]'] # локатор для раскрытия выпадающего списка на какой срок будет заказан самока
term_of_use = [By.XPATH, '//div[text()="четверо суток"]']   # локаор для поля выбора на сколько дней использовать
comment_for_delivery = [By.XPATH, '//input[@placeholder="Комментарий для курьера"]'] # локатор для формы коментария курьеру
button_take_order = [By.XPATH, '//button[@class="Button_Button__ra12g Button_Middle__1CSJM"]']  # локатор для кнопки заказать заказ
collor_scooter = [By.XPATH, '//input[@id="grey"]']  # локатор чек бокса цвета самоката цвет серый
button_confirm_order = [By.XPATH, '/html/body/div/div/div[2]/div[5]/div[2]/button[2]']  # кнопка ДА в модельном окне подтверждения заказа
arenda = [By.XPATH, '//div[@class="Order_Header__BZXOb"]']  # локатор написи Аренда
