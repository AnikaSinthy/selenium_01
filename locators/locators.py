from selenium.webdriver.common.by import By


class Locators():
    username = By.NAME, "username"
    password = By.NAME, "password"
    loginButton = By.XPATH, "//button[@id='submit']"
    logoutButton = By.XPATH, "//a[@href='https://practicetestautomation.com/practice-test-login/']"
    successfullyMsg = By.XPATH, '//h1'
