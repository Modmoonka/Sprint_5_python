from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from config import Variables, Waiter
from locators import *
from user import User

class TestAddCreating:

    #Создание объявления неавторизованным пользователем
    def test_add_creation_with_login_not_authorized(self, driver):
        # Клик на кнопку «Разместить объявление»
        driver.find_element(*MainPage.CREATION_BUTTON).click()
        # Ожидание загрузки формы создания объявления
        form_creation = WebDriverWait(driver, Waiter.WAIT_TIME).until(expected_conditions.visibility_of_element_located(CreationPage.REGISTRATION_LABEL))
        # Проверить: отображается модальное окно с заголовком «Чтобы разместить объявление, авторизуйтесь»
        assert form_creation.is_displayed() and form_creation.text.strip() == Variables.LABEL_AUTHORIZATION

    def test_add_creation_with_authorized_user(self, driver):
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
        # Ожидаем загрузку логотипа
        WebDriverWait(driver, Waiter.WAIT_TIME).until(expected_conditions.visibility_of_element_located(MainPage.AVATAR_LOGO))
        # Клик на кнопку «Разместить объявление»
        driver.find_element(*MainPage.CREATION_BUTTON).click()
        # Ожидание загрузки формы создания объявления
        WebDriverWait(driver, Waiter.WAIT_TIME).until(expected_conditions.visibility_of_element_located(CreationPage.CREATION_MASSAGE))

        # Заполнение полей
        driver.find_element(*CreationPage.TITLE).send_keys(Variables.TITLE_LABEL_TEST)
        driver.find_element(*CreationPage.PRODUCT_DESCRIPTION).send_keys(Variables.PRODUCT_DESCRIPTION_LABEL_TEST)
        driver.find_element(*CreationPage.PRICE).send_keys(Variables.PRICE_TEST)

        # Открываем дропдаун категорию
        driver.find_element(*Dropdowns.CATEGORY).click()
        WebDriverWait(driver, Waiter.WAIT_TIME).until(expected_conditions.visibility_of_element_located(Dropdowns.CATEGORY_AUTO))
        driver.find_element(*Dropdowns.CATEGORY_AUTO).click()

        # Клик дропдаун города
        driver.find_element(*Dropdowns.CITY).click()
        WebDriverWait(driver, Waiter.WAIT_TIME).until(expected_conditions.visibility_of_element_located(Dropdowns.CITY_CHOICE))
        # Клик дропдаун выбора города
        driver.find_element(*Dropdowns.CITY_CHOICE).click()

        # Выбрать RabioButton «Состояние товара»
        driver.find_element(*RadioButton.CONDITION["used"]).click()

        # Клик по кнопке "Опубликовать"
        driver.find_element(*CreationPage.PUBLISH_BUTTON).click()

        # Переход в профиль
        driver.refresh()
        WebDriverWait(driver, Waiter.WAIT_TIME).until(expected_conditions.visibility_of_element_located(MainPage.AVATAR_LOGO))
        # Клик по кнопке аватару
        driver.find_element(*MainPage.AVATAR_LOGO).click()
        WebDriverWait(driver, Waiter.WAIT_TIME).until(expected_conditions.visibility_of_element_located(Profile.PROFILE))
        # Ожидание появления надписи
        WebDriverWait(driver,  Waiter.WAIT_TIME).until(expected_conditions.visibility_of_element_located(Profile.CREATION))

        # Проверить наличие созданного объявления в списке объявлений
        WebDriverWait(driver, Waiter.WAIT_TIME).until(expected_conditions.element_to_be_clickable(Profile.CARD_ADD))
        ad_verification = driver.find_elements(*Profile.CARD_ADD)
        assert len(ad_verification) > 0, Variables.ERROR_TEXT_ADD_CREATION