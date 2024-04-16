import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class Base_Page(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.driver.set_page_load_timeout(60)
        self.driver.maximize_window()
        time.sleep(5)
        print("I am running from setUp method")

    def tearDown(self):
        self.driver.close()
        print("I am running from tearDown method")

    def test_valid_login(self):
        self.driver.find_element(By.NAME, "username").send_keys("Admin")
        time.sleep(5)
        self.driver.find_element(By.NAME, "password").send_keys("admin123")
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(5)
        elementValue = self.driver.find_element(By.XPATH, "//h6").text
        assert "Dashboard" == elementValue
        self.driver.find_element(By.XPATH, "//p").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//a[@href='/web/index.php/auth/logout']").click()
        time.sleep(2)
        print("I am running from test_valid_login method")

    def test_invalid_login_01(self):
        self.driver.find_element(By.NAME, "username").send_keys("ADMIN")
        time.sleep(5)
        self.driver.find_element(By.NAME, "password").send_keys("admin123")
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(5)
        print("I am running from test_invalid_login_01 method")

    def test_invalid_login_02(self):
        self.driver.find_element(By.NAME, "username").send_keys("Admin")
        time.sleep(5)
        self.driver.find_element(By.NAME, "password").send_keys("123ADMIN")
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(5)
        print("I am running from test_invalid_login_02 method")

    def test_invalid_login_03(self):
        self.driver.find_element(By.NAME, "username").send_keys("ADMIN")
        time.sleep(5)
        self.driver.find_element(By.NAME, "password").send_keys("Admin")
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(5)
        print("I am running from test_invalid_login_03 method")
