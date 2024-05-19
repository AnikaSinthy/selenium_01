import time

from tests.base_test import Base_Test
from pages.login_page import LoginPage
from testdata.test_data import TestData as DATA


class LoginTest(Base_Test):

    def test_valid_login(self):
        lp = LoginPage(self.driver)
        lp.enter_username(DATA.VALID_USERNAME)
        lp.enter_password(DATA.VALID_PASSWORD)
        lp.click_on_submit_button()
        lp.verify_the_we_are_logedin_successfully()
        time.sleep(5)

    def test_invalid_login_01(self):
        # self.driver.find_element(By.NAME, "username").send_keys("student1")
        # time.sleep(5)
        # self.driver.find_element(By.NAME, "password").send_keys("Password123")
        # time.sleep(5)
        # self.driver.find_element(By.XPATH, "//button[@id='submit']").click()
        # time.sleep(5)

        lp = LoginPage(self.driver)
        lp.enter_username(DATA.INVALID_USERNAME)
        lp.enter_password(DATA.VALID_PASSWORD)
        lp.click_on_submit_button()

        print("I am running from test_invalid_login_01 method")

    def test_invalid_login_02(self):
        # self.driver.find_element(By.NAME, "username").send_keys("student")
        # time.sleep(5)
        # self.driver.find_element(By.NAME, "password").send_keys("123Password")
        # time.sleep(5)
        # self.driver.find_element(By.XPATH, "//button[@id='submit']").click()
        # time.sleep(5)

        lp = LoginPage(self.driver)
        lp.enter_username(DATA.VALID_USERNAME)
        lp.enter_password(DATA.INVALID_PASSWORD)
        lp.click_on_submit_button()
        print("I am running from test_invalid_login_02 method")

    def test_invalid_login_03(self):
        # self.driver.find_element(By.NAME, "username").send_keys("Student")
        # time.sleep(5)
        # self.driver.find_element(By.NAME, "password").send_keys("Password")
        # time.sleep(5)
        # self.driver.find_element(By.XPATH, "//button[@id='submit']").click()
        # time.sleep(5)

        lp = LoginPage(self.driver)
        lp.enter_username(DATA.INVALID_USERNAME)
        lp.enter_password(DATA.INVALID_PASSWORD)
        lp.click_on_submit_button()
        print("I am running from test_invalid_login_03 method")
