import time

from selenium.webdriver.common.by import By


class LoginPage():

    def __init__(self, driver):
        self.driver = driver

        self.username = By.NAME, "username"
        self.password = By.NAME, "password"
        self.loginButton = By.XPATH, "//button[@id='submit']"
        self.logoutButton = By.XPATH, "//a[@href='https://practicetestautomation.com/practice-test-login/']"

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
        self.driver.find_element(*self.username).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.password).send_keys(password)
        time.sleep(5)

    def click_on_submit_button(self):
        self.driver.find_element(*self.loginButton).click()
        time.sleep(5)

    def verify_the_we_are_logedin_successfully(self):
        elementValue = self.driver.find_element(By.XPATH, "//h1").text
        assert "Logged In Successfully" == elementValue

    def click_on_logout_button(self):
        self.driver.find_element(*self.logoutButton).click()
