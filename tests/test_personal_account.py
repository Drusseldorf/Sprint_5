from test_data import URL
from locators import MainPage

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class TestPersonalAccount:

    def test_open_pers_acc_page_opened(self, driver, log_in):

        driver.find_element(*MainPage.ACCOUNT_BUTTON).click()

        WebDriverWait(driver, 3).until(ec.url_to_be(URL.PERSONAL_ACCOUNT_PAGE))

        assert driver.current_url == URL.PERSONAL_ACCOUNT_PAGE
