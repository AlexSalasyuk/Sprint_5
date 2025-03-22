from data import registered_user
from locators import *
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

def test_personal_account(driver):
    WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)).click()
    WebDriverWait(driver, 5).until(expected_conditions.url_contains('/login'))
    driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(registered_user['email'])
    driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(registered_user['password'])
    driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
    WebDriverWait(driver, 5).until_not(expected_conditions.url_contains('/login'))
    WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)).click()
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(AccountPageLocators.LOGOUT_BUTTON))
    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/account/profile'
