from locators import MainPage, ProfilePage
from test_data import URL

from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class TestExit:

    def test_exit_login_page_opened(self, driver, log_in):

        driver.find_element(*MainPage.ACCOUNT_BUTTON).click()

        WebDriverWait(driver, 3).until(ec.presence_of_element_located(ProfilePage.EXIT))
        driver.find_element(*ProfilePage.EXIT).click()

        WebDriverWait(driver, 3).until(ec.url_to_be(URL.LOGIN_PAGE))

        assert driver.current_url == URL.LOGIN_PAGE
