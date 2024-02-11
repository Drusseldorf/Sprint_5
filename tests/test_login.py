from test_data import AuthData
from locators import MainPage, LoginPage, RegistrationPage, ForgotPasswordPage

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class TestLogin:

    def test_login_to_acc_valid_data_button_make_order_present(self, driver):

        driver.find_element(*MainPage.LOGIN_BUTTON).click()

        driver.find_element(*LoginPage.EMAIL_INPUT).send_keys(AuthData.EMAIL)
        driver.find_element(*LoginPage.PASSWORD_INPUT).send_keys(AuthData.PASSWORD)
        driver.find_element(*LoginPage.LOGIN_BUTTON).click()

        WebDriverWait(driver, 3).until(ec.text_to_be_present_in_element(MainPage.MAKE_ORDER, 'Оформить заказ'))

        assert driver.find_element(*MainPage.MAKE_ORDER).text == 'Оформить заказ'

    def test_through_acc_valid_data_button_make_order_present(self, driver):

        driver.find_element(*MainPage.ACCOUNT_BUTTON).click()

        driver.find_element(*LoginPage.EMAIL_INPUT).send_keys(AuthData.EMAIL)
        driver.find_element(*LoginPage.PASSWORD_INPUT).send_keys(AuthData.PASSWORD)
        driver.find_element(*LoginPage.LOGIN_BUTTON).click()

        WebDriverWait(driver, 3).until(ec.text_to_be_present_in_element(MainPage.MAKE_ORDER, 'Оформить заказ'))

        assert driver.find_element(*MainPage.MAKE_ORDER).text == 'Оформить заказ'

    def test_through_reg_valid_data_button_make_order_present(self, driver):

        driver.find_element(*MainPage.ACCOUNT_BUTTON).click()

        driver.find_element(*LoginPage.REGISTER_BUTTON).click()

        driver.find_element(*RegistrationPage.LOGIN).click()

        driver.find_element(*LoginPage.EMAIL_INPUT).send_keys(AuthData.EMAIL)
        driver.find_element(*LoginPage.PASSWORD_INPUT).send_keys(AuthData.PASSWORD)
        driver.find_element(*LoginPage.LOGIN_BUTTON).click()

        WebDriverWait(driver, 3).until(ec.text_to_be_present_in_element(MainPage.MAKE_ORDER, 'Оформить заказ'))

        assert driver.find_element(*MainPage.MAKE_ORDER).text == 'Оформить заказ'

    def test_through_forgot_pass_valid_data_button_make_order_present(self, driver):

        driver.find_element(*MainPage.LOGIN_BUTTON).click()

        driver.find_element(*LoginPage.RESET_PASSWORD).click()

        driver.find_element(*ForgotPasswordPage.RESET_PASSWORD).click()

        driver.find_element(*LoginPage.EMAIL_INPUT).send_keys(AuthData.EMAIL)
        driver.find_element(*LoginPage.PASSWORD_INPUT).send_keys(AuthData.PASSWORD)
        driver.find_element(*LoginPage.LOGIN_BUTTON).click()

        WebDriverWait(driver, 3).until(ec.text_to_be_present_in_element(MainPage.MAKE_ORDER, 'Оформить заказ'))

        assert driver.find_element(*MainPage.MAKE_ORDER).text == 'Оформить заказ'
