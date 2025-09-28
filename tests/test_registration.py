from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from config import Variables, Waiter
from random_user import *
from locators import *
from user import User

class TestRegistration:

    def test_registration_valid_user(self, driver):
        # Клик по кнопке "Вход и регистрация"
        driver.find_element(*MainPage.LOGIN_BUTTON).click()
        #Клик по кнопке "Нет аккаунта"
        driver.find_element(*LoginPage.BUTTON_NO_REGISTER).click()

        # Ожидание загрузки формы регистрации
        WebDriverWait(driver, Waiter.WAIT_TIME).until(expected_conditions.visibility_of_element_located(RegistartionPage.REGISTRATION_FORM))
        
        # Заполняем все поля формы регистрации
        WebDriverWait(driver, Waiter.WAIT_TIME).until(expected_conditions.element_to_be_clickable(LoginPage.EMAIL)).send_keys(Random.generate_random_valid_email())
        correct_password = Random.valid_password()
        WebDriverWait(driver, Waiter.WAIT_TIME).until(expected_conditions.element_to_be_clickable(LoginPage.PASSWORD)).send_keys(correct_password)
        WebDriverWait(driver, Waiter.WAIT_TIME).until(expected_conditions.element_to_be_clickable(RegistartionPage.PASSWORD_REPEAT)).send_keys(correct_password)

        #Клик по кнопке «Создать аккаунт»
        driver.find_element(*RegistartionPage.BUTTON_CREATE).click()

        WebDriverWait(driver, Waiter.WAIT_TIME).until(expected_conditions.url_contains("/regiatration"))

        #Проверить: произошёл переход на главную страницу, в правом верхнем углу около кнопки «Разместить объявление» отображается аватар пользователя и имя User.
        user_element = WebDriverWait(driver, Waiter.WAIT_TIME).until(expected_conditions.visibility_of_element_located(MainPage.USER))
        avatar_logo = driver.find_element(*MainPage.AVATAR_LOGO)

        assert user_element.is_displayed() and user_element.text.strip() == "User." and avatar_logo.is_displayed()


    # Регистрация пользователя c email не по маске *******@*******.***
    def test_registration_incorrect_format_email(self, driver):
        # Клик по кнопке "Вход и регистрация"
        driver.find_element(*MainPage.LOGIN_BUTTON).click()
        #Клик по кнопке "Нет аккаунта"
        driver.find_element(*LoginPage.BUTTON_NO_REGISTER).click()

        # Ожидание загрузки формы регистрации
        WebDriverWait(driver, Waiter.WAIT_TIME).until(expected_conditions.visibility_of_element_located(RegistartionPage.REGISTRATION_FORM))
        
        # Заполнить поле Email формы регистрации
        WebDriverWait(driver, Waiter.WAIT_TIME).until(expected_conditions.element_to_be_clickable(LoginPage.EMAIL)).send_keys(Random.generate_random_invalid_email())
        correct_password = Random.valid_password()
        WebDriverWait(driver, Waiter.WAIT_TIME).until(expected_conditions.element_to_be_clickable(LoginPage.PASSWORD)).send_keys(correct_password)
        WebDriverWait(driver, Waiter.WAIT_TIME).until(expected_conditions.element_to_be_clickable(RegistartionPage.PASSWORD_REPEAT)).send_keys(correct_password)

        # Клик по кнопке «Создать аккаунт»
        driver.find_element(*RegistartionPage.BUTTON_CREATE).click()

        # Проверить: поля Email, «Пароль», «Повторите пароль» выделены красным, под полем Email отображается сообщение «Ошибка»
        WebDriverWait(driver, Waiter.WAIT_TIME).until(expected_conditions.visibility_of_element_located(RegistartionPage.TEXT_REGISTRATION))

        # Находим элемент с текстом ошибки
        text_error_message = driver.find_element(*RegistartionPage.TEXT_REGISTRATION)
        # Проверяем, что он отображается и содержит текст "Ошибка"
        error_text = text_error_message.is_displayed() and text_error_message.text.strip() == Variables.ERROR_LABEL
        # Проверяем, что все три поля подсвечены красным цветом
        error_fields_red = all([
            driver.find_element(*RegistartionPage.EMAIL_FIELD).is_displayed(),
            driver.find_element(*RegistartionPage.PASSWORD_FIELD).is_displayed(),
            driver.find_element(*RegistartionPage.REPEAT_PASSWORD_FIELD).is_displayed()
        ])
        assert error_text and error_fields_red

    # Регистрация уже существующего пользователя
    def test_registration_with_correct_user(self, driver):
        # Клик по кнопке "Вход и регистрация"
        driver.find_element(*MainPage.LOGIN_BUTTON).click()
        #Клик по кнопке "Нет аккаунта"
        driver.find_element(*LoginPage.BUTTON_NO_REGISTER).click()

        # Ожидание загрузки формы регистрации
        WebDriverWait(driver, Waiter.WAIT_TIME).until(expected_conditions.visibility_of_element_located(RegistartionPage.REGISTRATION_FORM))

        # Заполнить все поля формы регистрации данными уже существующего в системе пользователя
        driver.find_element(*LoginPage.EMAIL).send_keys(User.email)
        driver.find_element(*LoginPage.PASSWORD).send_keys(User.password)
        driver.find_element(*RegistartionPage.PASSWORD_REPEAT).send_keys(User.password)

        # Клик по кнопке «Создать аккаунт»
        driver.find_element(*RegistartionPage.BUTTON_CREATE).click()

        # Ожидание появления ошибки
        WebDriverWait(driver, Waiter.WAIT_TIME).until(expected_conditions.visibility_of_element_located(RegistartionPage.TEXT_REGISTRATION))

        # Находим элемент с текстом ошибки
        error_message_email = driver.find_element(*RegistartionPage.TEXT_REGISTRATION)
        # Проверяем, что он отображается и содержит нужный текст
        error_text_correct = error_message_email.is_displayed() and error_message_email.text.strip() == "Ошибка"
        # Проверяем, что все три поля подсвечены красным (видимы)
        error_fields_red = all([
            driver.find_element(*RegistartionPage.EMAIL_FIELD).is_displayed(),
            driver.find_element(*RegistartionPage.PASSWORD_FIELD).is_displayed(),
            driver.find_element(*RegistartionPage.REPEAT_PASSWORD_FIELD).is_displayed()
        ])
        assert error_text_correct and error_fields_red