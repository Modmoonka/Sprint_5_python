from selenium.webdriver.common.by import By


class MainPage:
    LOGIN_BTN = (By.XPATH, "//button[contains(text(), 'Вход и регистрация')]")
    LOGOUT_BTN = (By.XPATH, "//button[text()='Выйти']")
    CREATE_AD_BUTTON = (By.XPATH, "//button[text()='Разместить объявление']")
    USER_NAME = (By.CSS_SELECTOR, "h3.profileText.name")
    AVATAR_LOGO = (By.CSS_SELECTOR, "button.circleSmall")


class LoginPage:
    LOGIN = (By.XPATH, "//h1[text()='Войти']")
    EMAIL = (By.NAME, 'email')
    PASSWORD = (By.NAME, 'password')
    BUTTON_LOGIN = (By.XPATH, "//button[text()='Войти']")
    BUTTON_NO_REGISTER = (By.XPATH, "//button[text()='Нет аккаунта']")


class RegistartionPage:
    LABEL_REGISTRATION = (By.XPATH, "//h1[text()='Зарегистрироваться']")
    CONFIRM_PASSWORD_INPUT = (By.NAME, 'submitPassword')

    BUTTON_CREATE = (By.XPATH, "//button[text()='Создать аккаунт']")
    EMAIL_ERROR = (By.XPATH, "//span[@class='input_span__yWPqB' and text()='Ошибка']")


class AdvertisementPageLocators:

    DESCRIPTION_TEXTAREA = (By.XPATH, "//textarea[@placeholder='Описание товара']")
    PRICE_INPUT = (By.NAME, "price")
    CATEGORY_DROPDOWN = (By.CSS_SELECTOR, "input[name='category'] + button")
    CATEGORY_OPTIONS = ((By.XPATH, "//div[@class='dropDownMenu_options__CmHmm']/button"))
    LAST_CATEGORY = (By.XPATH, "(//div[@class='dropDownMenu_options__CmHmm']/button)[last()]")
    CITY_DROPDOWN = (By.CSS_SELECTOR, "input[name='city'] + button")
    CITY_OPTIONS = (By.XPATH, "//div[@data-test='city-select-menu']//button")
    LAST_CITY_OPTION = (By.XPATH, "(//div[@class='dropDownMenu_options__CmHmm']/button)[last()]")
    CONDITION_RADIOBUTTON_NEW = (By.XPATH, "//div[@class='radioUnput_inputActive__eC-HY']")
    CONDITION_RADIOBUTTON_USED = (By.XPATH, "//div[@class='radioUnput_inputRegular__FbVbr']")
    SUBMIT_BUTTON = (By.XPATH, "//button[text()='Опубликовать']")
    AUTH_ERROR = (By.XPATH, "//h1[text()='Чтобы разместить объявление, авторизуйтесь']")


class ProfilePageLocators:
    MY_ADS_SECTION = (By.XPATH,
                      "//h1[contains(text(),'Мои объявления')]/following-sibling::div//div[@class='grid_threeColumns__ldn5D']")
    AD_TITLE = (By.XPATH, ".//h2[@class='h2']")
    AD_CARDS = (By.XPATH, "//div[contains(@class, 'grid_threeColumns__ldn5D')]//div[@class='card']")