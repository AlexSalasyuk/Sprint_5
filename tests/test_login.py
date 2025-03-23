from data import registered_user
from locators import *
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from urls import BASE_URL, REGISTER_URL, FORGOT_PASSWORD_URL

def test_login_main_page(driver):
    WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(MainPageLocators.LOGIN_BUTTON)).click()
    WebDriverWait(driver, 5).until(expected_conditions.url_contains('/login'))
    driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(registered_user['email'])
    driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(registered_user['password'])
    driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
    WebDriverWait(driver, 5).until_not(expected_conditions.url_contains('/login'))
    assert driver.current_url == BASE_URL

def test_login_personal_account_button(driver):
    WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)).click()
    WebDriverWait(driver, 5).until(expected_conditions.url_contains('/login'))
    driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(registered_user['email'])
    driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(registered_user['password'])
    driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
    WebDriverWait(driver, 5).until_not(expected_conditions.url_contains('/login'))
    assert driver.current_url == BASE_URL

def test_login_registration_page(driver):
    driver.get(REGISTER_URL)
    WebDriverWait(driver,5).until(expected_conditions.element_to_be_clickable(RegistrationPageLocators.REGISTER_LOGIN_LINK)).click()
    WebDriverWait(driver, 5).until(expected_conditions.url_contains('/login'))
    driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(registered_user['email'])
    driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(registered_user['password'])
    driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
    WebDriverWait(driver, 5).until_not(expected_conditions.url_contains('/login'))
    assert driver.current_url == BASE_URL

def test_login_recovery_page(driver):
    driver.get(FORGOT_PASSWORD_URL)
    WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(PasswordRecoveryPageLocators.RECOVERY_LOGIN_LINK)).click()
    WebDriverWait(driver, 5).until(expected_conditions.url_contains('/login'))
    driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(registered_user['email'])
    driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(registered_user['password'])
    driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
    WebDriverWait(driver, 5).until_not(expected_conditions.url_contains('/login'))
    assert driver.current_url == BASE_URL
