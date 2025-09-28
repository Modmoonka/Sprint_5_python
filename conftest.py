import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import *
from selenium import webdriver
from random_user import *

@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Chrome()
    driver.get("https://qa-desk.stand.praktikum-services.ru/")
    yield driver
    driver.quit()

@pytest.fixture
def unique_valid_email():
    return generate_random_valid_email()

@pytest.fixture
def unique_invalid_email():
    return generate_invalid_unique_email()

@pytest.fixture
def login_user(driver):
    # Клик по кнопке "Вход и регистрация"
    driver.find_element(*MainPage.LOGIN_BTN).click()

    # Вводим логин и пароль
    driver.find_element(*LoginPage.EMAIL).send_keys('babatenko_25@gmail.com')
    driver.find_element(*LoginPage.PASSWORD).send_keys('123qwe')

    # Клик по кнопке "Войти"
    driver.find_element(*LoginPage.BUTTON_LOGIN).click()

    # Ожидаем, что пользователь авторизовался (например, по появлению аватара или имени)
    WebDriverWait(driver, Waiter.WAIT_TIME).until(
        expected_conditions.visibility_of_element_located(MainPage.USER_NAME)
    )
    return driver