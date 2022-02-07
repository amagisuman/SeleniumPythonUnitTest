import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

from utilities.BaseClass import BaseClass
from pageObjects.Login import LoginPage
from pageObjects.Overview import Overview
from pageObjects.Logout import Logout
from selenium.webdriver.support.ui import Select


class LoginTest(unittest.TestCase):
    baseURL = "https://analytics.amagi.tv"
    username = "suman.kumar@amagi.com"
    password = ""
    driver = webdriver.Firefox()

    @classmethod
    def setUpClass(cls):
        cls.driver.get(cls.baseURL)
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(5)

    def test_Login(self):
        lp = LoginPage(self.driver)
        lp.setUserName(self.username)
        lp.setPassword(self.password)
        lp.clickLogin()
        time.sleep(7)
        act_title = self.driver.title
        # Capture screenshots when steps will fail
        if act_title == "Amagi Analytics":
            assert True
        else:
            self.driver.save_screenshot("./Screenshot_" + "test_Login.png")
            self.driver.close()
            assert False
        time.sleep(5)

    def test_Overview(self):
        ov = Overview(self.driver)
        time.sleep(5)
        ov.customerSelection()
        time.sleep(3)
        ov.dataIntervalSelection()
        time.sleep(3)
        ov.filterBySelection()
        time.sleep(1)
        ov.dailyMetricsSelection()
        ov.regionalMetricsSelection()
        ov.contentMetricsSelection()
        ov.hourlySelection()
        time.sleep(3)
        ov.clickLogout()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()
