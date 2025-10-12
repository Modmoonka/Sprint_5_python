from selenium.webdriver.common.by import By

class MainPage:
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(), 'Вход и регистрация')]")
    CREATION_BUTTON = (By.XPATH, "//button[text()='Разместить объявление']")
    USER = (By.CSS_SELECTOR, "h3.profileText.name")
    AVATAR_LOGO = (By.CSS_SELECTOR, "button.circleSmall")


class LoginPage:
    EMAIL = (By.NAME, 'email')
    PASSWORD = (By.NAME, 'password')
    BUTTON_NO_REGISTER = (By.XPATH, "//button[text()='Нет аккаунта']")
    LOGIN = (By.XPATH, "//h1[text()='Войти']")
    LOGIN_BUTTON = (By.XPATH, "//button[@type='submit' and contains(@class, 'buttonPrimary') and text()='Войти']")
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выйти']")


class RegistartionPage:
    REGISTRATION_FORM = (By.XPATH, "//h1[text()='Зарегистрироваться']")
    PASSWORD_REPEAT = (By.NAME, 'submitPassword')
    BUTTON_CREATE = (By.XPATH, "//button[text()='Создать аккаунт']")
    EMAIL_FIELD = (By.CSS_SELECTOR, 'div.input_inputError__fLUP9 input[name="email"]')
    PASSWORD_FIELD = (By.CSS_SELECTOR, 'div.input_inputError__fLUP9 input[name="password"]')
    REPEAT_PASSWORD_FIELD = (By.CSS_SELECTOR, 'div.input_inputError__fLUP9 input[name="submitPassword"]')
    TEXT_REGISTRATION = (By.CLASS_NAME, "input_span__yWPqB")


class CreationPage:
    CREATION_MASSAGE = (By.XPATH, "//h1[text()='Новое объявление']")
    REGISTRATION_LABEL = (By.XPATH, "//h1[text()='Чтобы разместить объявление, авторизуйтесь']")
    PRODUCT_DESCRIPTION = (By.XPATH, "//textarea[@placeholder='Описание товара']")
    TITLE = (By.CSS_SELECTOR, 'input[name="name"]')
    PRICE = (By.CSS_SELECTOR, 'input[name="price"]')
    PUBLISH_BUTTON = (By.XPATH, "//button[text()='Опубликовать']")

class Dropdowns:
        CITY = (By.CSS_SELECTOR, 'div.dropDownMenu_input__itKtw input[name="city"] + button')
        CATEGORY = (By.CSS_SELECTOR, 'div.dropDownMenu_input__itKtw input[name="category"] + button')
        CITY_CHOICE= (By.XPATH, '//button[.//span[text()="Санкт-Петербург"]]')
        CATEGORY_AUTO = (By.XPATH, '//button[.//span[text()="Авто"]]')

class RadioButton:
            CONDITION = {
                "new": (By.XPATH, '//div[@class="radioUnput_shell__Wtdwe"][.//label[text()="Новый"]]'),
                "used": (By.XPATH, '//div[@class="radioUnput_shell__Wtdwe"][.//label[text()="Б/У"]]'),
            }

class Profile:
    PROFILE = (By.XPATH, '//h1[text()="Мой профиль"]')
    CREATION = (By.XPATH, '//h1[text()="Мои объявления"]')
    CARD_ADD= (By.XPATH, "//div[contains(@class, 'grid_threeColumns__ldn5D')]//div[@class='card']")

