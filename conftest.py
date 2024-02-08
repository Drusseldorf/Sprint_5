import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

import helpers
from locators import MainPage, LoginPage
from test_data import URL, AuthData


@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.set_window_size(1920, 1080)
    driver.get(URL.MAIN_PAGE)
    yield driver
    driver.quit()


@pytest.fixture(scope='function')
def random_email():
    email = helpers.random_valid_email()
    return email


@pytest.fixture(scope='function')
def random_password():
    password = helpers.random_valid_password()
    return password


@pytest.fixture(scope='function')
def log_in(driver):
    driver.find_element(*MainPage.LOGIN_BUTTON).click()
    driver.find_element(*LoginPage.EMAIL_INPUT).send_keys(AuthData.EMAIL)
    driver.find_element(*LoginPage.PASSWORD_INPUT).send_keys(AuthData.PASSWORD)
    driver.find_element(*LoginPage.LOGIN_BUTTON).click()
