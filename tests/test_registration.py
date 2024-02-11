from test_data import RegistrationData, URL
from locators import MainPage, LoginPage, RegistrationPage
from helpers import RandomCreds

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class TestRegistration:

    def test_registration_valid_data_redirected_to_login(self, driver):

        driver.find_element(*MainPage.ACCOUNT_BUTTON).click()

        driver.find_element(*LoginPage.REGISTER_BUTTON).click()

        driver.find_element(*RegistrationPage.NAME_INPUT).send_keys(RegistrationData.VALID_NAME)
        driver.find_element(*RegistrationPage.EMAIL_INPUT).send_keys(RandomCreds.email())
        driver.find_element(*RegistrationPage.PASSWORD_INPUT).send_keys(RandomCreds.password())
        driver.find_element(*RegistrationPage.REGISTER_BUTTON).click()

        WebDriverWait(driver, 3).until(ec.url_to_be(URL.LOGIN_PAGE))

        assert driver.current_url == URL.LOGIN_PAGE

    def test_registration_password_less_6_chars_error_appeared(self, driver):

        driver.find_element(*MainPage.ACCOUNT_BUTTON).click()

        driver.find_element(*LoginPage.REGISTER_BUTTON).click()

        driver.find_element(*RegistrationPage.NAME_INPUT).send_keys(RegistrationData.VALID_NAME)
        driver.find_element(*RegistrationPage.EMAIL_INPUT).send_keys(RandomCreds.email())
        driver.find_element(*RegistrationPage.PASSWORD_INPUT).send_keys(RegistrationData.PASSWORD_LESS_6)
        driver.find_element(*RegistrationPage.REGISTER_BUTTON).click()

        assert driver.find_element(*RegistrationPage.INVALID_PASSWORD_ERROR).text == 'Некорректный пароль'
