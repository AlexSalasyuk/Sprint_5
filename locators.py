from selenium.webdriver.common.by import By

class RegistrationPageLocators: # локаторы страницы регистрации
    NAME_INPUT = (By.XPATH, '//label[text()="Имя"]/following-sibling::input') # поле ввода имени
    EMAIL_INPUT = (By.XPATH, '//label[text()="Email"]/following-sibling::input') # поле ввода email
    PASSWORD_INPUT = (By.XPATH, '//label[text()="Пароль"]/following-sibling::input') # поле ввода пароля
    REGISTER_BUTTON = (By.XPATH, '//button[text()="Зарегистрироваться"]') # кнопка регистрации
    ERROR_MESSAGE = (By.XPATH, '//p[text()="Некорректный пароль"]') # сообщение об ошибке
    REGISTER_LOGIN_LINK = (By.XPATH, '//a[text()="Войти"]') # ссылка войти на странице регистрации

class LoginPageLocators: # локаторы страницы входа
    EMAIL_INPUT = (By.XPATH, '//label[text()="Email"]/following-sibling::input') # поле ввода email
    PASSWORD_INPUT = (By.XPATH, '//label[text()="Пароль"]/following-sibling::input') # поле ввода пароля
    LOGIN_BUTTON = (By.XPATH, '//button[text()="Войти"]') # кнопка входа

class MainPageLocators: # локаторы главной страницы
    LOGIN_BUTTON = (By.XPATH, '//button[text()="Войти в аккаунт"]') # кнопка входа в аккаунт
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, '//p[text()="Личный Кабинет"]') # кнопка личного кабинета
    CONSTRUCTOR_BUTTON = (By.XPATH, '//p[text()="Конструктор"]') # кнопка конструктора
    LOGO_LINK = (By.XPATH, '//div[contains(@class, "AppHeader_header__logo")]/a') # лого stellar burgers
    BUNS_TAB = (By.XPATH, '//span[text()="Булки"]') # раздел булок
    SAUCES_TAB = (By.XPATH, '//span[text()="Соусы"]') # раздел соусов
    FILLINGS_TAB = (By.XPATH, '//span[text()="Начинки"]') # раздел начинок
    ACTIVE_TAB = (By.XPATH, '//*[contains(@class,"tab_tab_type_current")]') # активная вкладка

class AccountPageLocators: # локатор личного кабинета
    LOGOUT_BUTTON = (By.XPATH, '//button[text()="Выход"]') # кнопка выхода

class PasswordRecoveryPageLocators: # локатор страницы восстановления пароля
    RECOVERY_LOGIN_LINK = (By.XPATH, '//a[text()="Войти"]') # ссылка войти на странице восстановления пароля
