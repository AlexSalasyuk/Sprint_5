from data import registered_user
from locators import *
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from urls import BASE_URL


def test_redirect_by_constructor(driver):
    WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)).click()
    WebDriverWait(driver, 5).until(expected_conditions.url_contains('/login'))
    driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(registered_user['email'])
    driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(registered_user['password'])
    driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
    WebDriverWait(driver, 5).until_not(expected_conditions.url_contains('/login'))
    WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)).click()
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(MainPageLocators.CONSTRUCTOR_BUTTON)).click()
    WebDriverWait(driver, 5).until_not(expected_conditions.url_contains('/profile'))
    assert driver.current_url == BASE_URL

def test_redirect_by_logo(driver):
    WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)).click()
    WebDriverWait(driver, 5).until(expected_conditions.url_contains('/login'))
    driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(registered_user['email'])
    driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(registered_user['password'])
    driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
    WebDriverWait(driver, 5).until_not(expected_conditions.url_contains('/login'))
    WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)).click()
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(MainPageLocators.LOGO_LINK)).click()
    WebDriverWait(driver, 5).until_not(expected_conditions.url_contains('/profile'))
    assert driver.current_url == BASE_URL
