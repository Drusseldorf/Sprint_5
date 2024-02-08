from selenium.webdriver.common.by import By


class MainPage:
    """ Главная страница """

    ACCOUNT_BUTTON = By.CSS_SELECTOR, '[href="/account"]'  # Личный кабинет
    LOGIN_BUTTON = By.XPATH, '//button[text()="Войти в аккаунт"]'  # Войти в аккаунт
    MAKE_ORDER = By.XPATH, '//button[text()="Оформить заказ"]'  # Оформить заказ
    CONSTRUCTOR = By.XPATH, '//li/a[@href="/"]'  # Конструктор
    BURGER_BUN = By.XPATH, '//span[text()="Булки"]/parent::div'
    SAUCE = By.XPATH, '//span[text()="Соусы"]/parent::div'
    FILLING = By.XPATH, '//span[text()="Начинки"]/parent::div'


class LoginPage:
    """ Страница логина """

    EMAIL_INPUT = By.CSS_SELECTOR, '.input__textfield[type="text"]'  # Поле ввода email
    PASSWORD_INPUT = By.CSS_SELECTOR, '.input__textfield[type="password"]'  # Поле ввода пароля
    LOGIN_BUTTON = By.XPATH, '//button[text()="Войти"]'  # Войти
    REGISTER_BUTTON = By.CSS_SELECTOR, '[href="/register"]'  # Зарегистрироваться
    RESET_PASSWORD = By.XPATH, '//a[@href="/forgot-password"]'  # Восстановить пароль


class RegistrationPage:
    """ Страница регистрации """

    NAME_INPUT = By.XPATH, '(//input[@type="text"])[1]'  # Поле ввода имени
    EMAIL_INPUT = By.XPATH, '(//input[@type="text"])[2]'  # Поле ввода email
    PASSWORD_INPUT = By.CSS_SELECTOR, '.input__textfield[type="password"]'  # Поле ввода пароля
    REGISTER_BUTTON = By.XPATH, '//button[text()="Зарегистрироваться"]'  # Зарегистрироваться
    LOGIN = By.XPATH, '//a[@href="/login"]'  # войти
    INVALID_PASSWORD_ERROR = By.CSS_SELECTOR, '.input__error'  # ошибка неверного пароля


class ForgotPasswordPage:
    """ Страница восстановления пароля """

    RESET_PASSWORD = By.XPATH, '//a[@href="/login"]'


class ProfilePage:
    """ Страница личного кабинета """

    CONSTRUCTOR = By.XPATH, '//li/a[@href="/"]'  # Конструктор
    LOGO_STELLAR_BURGERS = By.XPATH, '//div/a[@href="/"]'  # Логотип Stellar Burgers
    EXIT = By.XPATH, '//li/button'  # Кнопка Выйти
