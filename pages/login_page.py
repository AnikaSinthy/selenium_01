import time

from selenium.webdriver.common.by import By
from locators.locators import Locators
from pages.base_page import BasePage


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.locator = Locators

    def login_to_application(self):
        self.driver.find_element(By.NAME, "username").send_keys("student")
        time.sleep(5)
        self.driver.find_element(By.NAME, "password").send_keys("Password123")
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//button[@id='submit']").click()
        time.sleep(5)
        elementValue = self.driver.find_element(By.XPATH, "//h1").text
        assert "Logged In Successfully" == elementValue
        self.driver.find_element(By.XPATH,
                                 "//a[@href='https://practicetestautomation.com/practice-test-login/']").click()
        print("I am running from test_valid_login method")

    def enter_username(self, username):
        # self.driver.find_element(*self.locator.username).send_keys(username)
        self.enter_at(self.locator.username, username)

    def enter_password(self, password):
        # self.driver.find_element(*self.locator.password).send_keys(password)
        self.enter_at(self.locator.password, password)
        time.sleep(5)

    def click_on_submit_button(self):
        # self.driver.find_element(*self.locator.loginButton).click()
        self.click_element(self.locator.loginButton)

        time.sleep(5)

    def verify_the_we_are_logedin_successfully(self):
        # elementValue = self.driver.find_element(By.XPATH, "//h1").text
        elementValue = self.get_text(self.locator.successfullyMsg)
        print(elementValue)
        assert "Logged In Successfully" == elementValue

    def click_on_logout_button(self):
        self.driver.find_element(*self.locator.logoutButton).click()
