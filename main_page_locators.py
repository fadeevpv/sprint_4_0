from selenium.webdriver.common.by import By

main_page = 'https://qa-scooter.praktikum-services.ru'  # ссылка на страницу

# локатор кнопки cookie
button_cookie = [By.XPATH, '//button[@id="rcc-confirm-button"]']

# локаторый кнопок оформления заказов
button1_get_order_on_top = [By.XPATH, '//button[@class="Button_Button__ra12g"]'] # кнопка оформления заказа  верхняя локатор можно переиспользовать в форме заказа
button2_get_order_after_scrolling = [By.XPATH, '//button[@class="Button_Button__ra12g Button_Middle__1CSJM"]'] # кнопка оформления заказа нижняя

# Локаторы блока вопросов
header_questions = [By.XPATH, '/html/body/div/div/div/div[5]/div[1]']  #заголовок блока вопросов о важном

first_question = [By.XPATH, '//div[@id="accordion__heading-0"]']   # вопрос первый

second_question = [By.XPATH, '//div[@id="accordion__heading-1"]']   # вопрос второй

third_question = [By.XPATH, '//div[@id="accordion__heading-2"]']    # вопрос третий

fourth_question = [By.XPATH, '//div[@id="accordion__heading-3"]']  # вопрос четвертый

fifth_question = [By.XPATH, '//div[@id="accordion__heading-4"]']   # вопрос пятый

sixth_question = [By.XPATH, '//div[@id="accordion__heading-5"]']  # вопрос шестой

seventh_question = [By.XPATH, '//div[@id="accordion__heading-6"]']  # вопрос седьмой

eighth_question = [By.XPATH, '//div[@id="accordion__heading-7"]']  # вопрос восьмой







