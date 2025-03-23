import pytest
import random
import string
from selenium import webdriver
from urls import BASE_URL

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get(BASE_URL)
    yield driver
    driver.quit()

@pytest.fixture
def generate_email():
    first_name = 'alex'
    last_name = 'salasyuk'
    cohort_number = '19'
    random_digits = ''.join(random.choices(string.digits, k=3))
    return f'{first_name}_{last_name}_{cohort_number}_{random_digits}@yandex.ru'

@pytest.fixture
def generate_password():
    length = random.randint(6, 8)
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))
