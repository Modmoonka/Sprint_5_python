from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from config import Waiter
from locators import *
from user import *

class TestLogin:

    def test_user_login(self, driver):
                # Клик по кнопке "Вход и регистрация"
        driver.find_element(*MainPage.LOGIN_BUTTON).click()
        # Ожидание загрузки страницы
        WebDriverWait(driver, Waiter.WAIT_TIME).until(expected_conditions.visibility_of_element_located(MainPage.LOGIN_BUTTON))
        # Ввод email
        WebDriverWait(driver, Waiter.WAIT_TIME).until(expected_conditions.element_to_be_clickable(LoginPage.EMAIL)).send_keys(User.email)
        # Ввод пароля
        WebDriverWait(driver, Waiter.WAIT_TIME).until(expected_conditions.element_to_be_clickable(LoginPage.PASSWORD)).send_keys(User.password)
        # Клик по кнопке "Войти"
        driver.find_element(*LoginPage.LOGIN_BUTTON).click()
        #Ожидаем загрузку логотипа
        WebDriverWait(driver, Waiter.WAIT_TIME).until(expected_conditions.visibility_of_element_located(MainPage.AVATAR_LOGO))

        # Проверить: произошёл переход на главную страницу, в правом верхнем углу около кнопки «Разместить объявление» отображается аватар пользователя и имя User.
        visible_user_element = WebDriverWait(driver, Waiter.WAIT_TIME).until(expected_conditions.visibility_of_element_located(MainPage.USER))
        logo = driver.find_element(*MainPage.AVATAR_LOGO)
        creation_button = driver.find_element(*MainPage.CREATION_BUTTON)
        assert visible_user_element.is_displayed() and visible_user_element.text.strip() == "User." \
                       and logo.is_displayed() and creation_button.is_displayed()

    # Logout пользователя
    def test_logout_user(self, driver):
        # Клик по кнопке "Вход и регистрация"
        driver.find_element(*MainPage.LOGIN_BUTTON).click()
        # Ожидание загрузки страницы
        WebDriverWait(driver, Waiter.WAIT_TIME).until(expected_conditions.visibility_of_element_located(MainPage.LOGIN_BUTTON))
        # Ввод email
        WebDriverWait(driver, Waiter.WAIT_TIME).until(expected_conditions.element_to_be_clickable(LoginPage.EMAIL)).send_keys(User.email)
        # Ввод пароля
        WebDriverWait(driver, Waiter.WAIT_TIME).until(expected_conditions.element_to_be_clickable(LoginPage.PASSWORD)).send_keys(User.password)
        # Клик по кнопке "Войти"
        driver.find_element(*LoginPage.LOGIN_BUTTON).click()
        # Ожидаем, пока появится имя пользователя
        WebDriverWait(driver, Waiter.WAIT_TIME).until(expected_conditions.visibility_of_element_located(MainPage.USER))
        # Клик по кнопке "Выйти"
        driver.find_element(*LoginPage.LOGOUT_BUTTON).click()
        # Ожидание появления кнопки «Вход и регистрация»
        WebDriverWait(driver, Waiter.WAIT_TIME).until(expected_conditions.visibility_of_element_located(MainPage.LOGIN_BUTTON))

        # Проверка наличия кнопки "Вход и регистрация"
        register_button = WebDriverWait(driver, Waiter.WAIT_TIME).until(expected_conditions.visibility_of_element_located(MainPage.LOGIN_BUTTON))

        #Проверить: аватар пользователя и имя User больше не отображается в правом верхнем углу около кнопки «Разместить объявление»
        assert register_button.is_displayed() and not driver.find_elements(*MainPage.AVATAR_LOGO) and not driver.find_elements(*MainPage.USER)