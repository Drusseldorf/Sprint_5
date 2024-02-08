from locators import MainPage
import time


class TestSwitchTabs:

    def test_switch_tabs_burgerbun_selected(self, driver):

        driver.find_element(*MainPage.SAUCE).click()
        driver.find_element(*MainPage.BURGER_BUN).click()

        class_atr = driver.find_element(*MainPage.BURGER_BUN).get_attribute('class')

        assert 'current' in class_atr

    def test_switch_tabs_sauce_selected(self, driver):

        driver.find_element(*MainPage.SAUCE).click()

        class_atr = driver.find_element(*MainPage.SAUCE).get_attribute('class')

        assert 'current' in class_atr

    def test_switch_tabs_filling_selected(self, driver):

        driver.find_element(*MainPage.FILLING).click()

        class_atr = driver.find_element(*MainPage.FILLING).get_attribute('class')

        assert 'current' in class_atr
