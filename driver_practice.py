import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class Base_Page(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://practicetestautomation.com/practice-test-login/")
        self.driver.maximize_window()
        time.sleep(5)
        print("I am running from setUp method")

    def tearDown(self):
        self.driver.close()
        print("I am running from tearDown method")

    def test_valid_login(self):
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

    def test_invalid_login(self):
        self.driver.find_element(By.NAME, "username").send_keys("student1")
        time.sleep(5)
        self.driver.find_element(By.NAME, "password").send_keys("Password123")
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//button[@id='submit']").click()
        time.sleep(5)
        print("I am running from test_invalid_login method")
