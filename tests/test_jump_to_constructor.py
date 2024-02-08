from locators import MainPage, ProfilePage


class TestJumpToConstructor:

    def test_jump_to_constructor_through_constructor(self, driver, log_in):

        driver.find_element(*MainPage.ACCOUNT_BUTTON).click()
        driver.find_element(*ProfilePage.CONSTRUCTOR).click()

        constructor_class = driver.find_element(*MainPage.CONSTRUCTOR).get_attribute('class')

        assert 'link_active' in constructor_class

    def test_jump_to_constructor_through_logo(self, driver, log_in):

        driver.find_element(*MainPage.ACCOUNT_BUTTON).click()
        driver.find_element(*ProfilePage.LOGO_STELLAR_BURGERS).click()

        constructor_class = driver.find_element(*MainPage.CONSTRUCTOR).get_attribute('class')

        assert 'link_active' in constructor_class
