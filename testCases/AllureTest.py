import pytest
from allure_commons.types import AttachmentType
from selenium.webdriver.chrome import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
import allure


@allure.severity(allure.severity_level.NORMAL)
class AllureTest:
    @allure.severity(allure.severity_level.MINOR)
    def test_Logo(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://analytics.amagi.tv")
        status = self.driver.find_element(By.XPATH, "//*[@id='root'']/div[1]/a[1]/svg/g/path").is_displayed()

        if status == True:
            assert True
        else:
            assert False
        self.driver.close()

    @allure.severity(allure.severity_level.NORMAL)
    def test_listemployees(self):
        pytest.skip("Skipping Test...")

    @allure.severity(allure.severity_level.CRITICAL)
    def test_login(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://analytics.amagi.tv")
        self.driver.maximize_window()
        self.driver.find_element(By.NAME, "email").send_keys("suman.kumar@amagi.com")
        self.driver.find_element(By.NAME, "password").send_keys("PDCED*vzu70")
        self.driver.find_element(By.XPATH, "//body[1]/div[1]/div[2]/div[2]/div[2]/form[1]/div[3]/button[1]").click()
        act_title = self.driver.title

        if act_title == "Amagi Analytics":
            self.driver.close()
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="testLoginScreen",
                          attachment_type=AttachmentType.PNG)
            self.driver.close()
            assert False
