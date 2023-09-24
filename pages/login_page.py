from selenium.webdriver.common.by import By

from browser import Browser


class Login(Browser):
    USERNAME_FIELD = (By.ID, "user-name")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BTN = (By.ID, "login-button")
    INVENTORY_PAGE_TITLE = (By.XPATH, "//span[@class='title']")
    ERROR_MSG = (By.XPATH, "//h3[@data-test='error']")
    USERNAME = "standard_user"
    PASSWORD = "secret_sauce"

    def open_login_page(self):
        self.driver.get("https://www.saucedemo.com/")

    def set_username(self, username):
        self.driver.find_element(*self.USERNAME_FIELD).send_keys(username)

    def set_password(self, password):
        self.driver.find_element(*self.PASSWORD_FIELD).send_keys(password)

    def click_login_btn(self):
        self.driver.find_element(*self.LOGIN_BTN).click()

    def login_into_app(self):
        self.open_login_page()
        self.set_username(self.USERNAME)
        self.set_password(self.PASSWORD)
        self.click_login_btn()

    def verify_successful_login(self):
        actual_result = self.driver.find_element(*self.INVENTORY_PAGE_TITLE).text
        expected_result = "Products"
        assert actual_result == expected_result, (f"Error: actual result {actual_result} is different than "
                                                  f"expected result {expected_result}")

    def verify_failed_login(self, expected_result):
        actual_result = self.driver.find_element(*self.ERROR_MSG).text
        assert actual_result == expected_result, (f"Error: actual result {actual_result} is different than "
                                                  f"expected result {expected_result}")
