from locators import *
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

def test_successful_registration(driver, generate_email, generate_password):
    email = generate_email
    password = generate_password
    driver.get('https://stellarburgers.nomoreparties.site/register')
    driver.find_element(*RegistrationPageLocators.NAME_INPUT).send_keys('Alex')
    driver.find_element(*RegistrationPageLocators.EMAIL_INPUT).send_keys(email)
    driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT).send_keys(password)
    driver.find_element(*RegistrationPageLocators.REGISTER_BUTTON).click()
    WebDriverWait(driver, 5).until(expected_conditions.url_contains('/login'))
    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'

def test_registration_with_short_password(driver, generate_email):
    email = generate_email
    driver.get('https://stellarburgers.nomoreparties.site/register')
    driver.find_element(*RegistrationPageLocators.NAME_INPUT).send_keys('Alex')
    driver.find_element(*RegistrationPageLocators.EMAIL_INPUT).send_keys(email)
    driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT).send_keys('0')
    driver.find_element(*RegistrationPageLocators.REGISTER_BUTTON).click()
    error_message = driver.find_element(*RegistrationPageLocators.ERROR_MESSAGE).text
    assert 'Некорректный пароль' in error_message
