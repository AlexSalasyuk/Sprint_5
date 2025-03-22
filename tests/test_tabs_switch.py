from locators import *
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

def test_tabs_switch(driver):
    driver.find_element(*MainPageLocators.SAUCES_TAB).click()
    active_tab = WebDriverWait(driver, 15).until(expected_conditions.visibility_of_element_located(MainPageLocators.ACTIVE_TAB))
    assert active_tab.text == 'Соусы'


    driver.find_element(*MainPageLocators.FILLINGS_TAB).click()
    active_tab = WebDriverWait(driver, 15).until(expected_conditions.visibility_of_element_located(MainPageLocators.ACTIVE_TAB))
    assert active_tab.text == 'Начинки'


    driver.find_element(*MainPageLocators.BUNS_TAB).click()
    active_tab = WebDriverWait(driver, 15).until(expected_conditions.visibility_of_element_located(MainPageLocators.ACTIVE_TAB))
    assert active_tab.text == 'Булки'
