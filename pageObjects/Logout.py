from selenium.webdriver.common.by import By


class Logout:
    # Logout
    logout_click_xpath = "//*[@id='root']/header/div/div[2]/button/span[1]/span[3]"
    button_logout_xpath = "/html/body/div[2]/div[3]/li"

    def __init__(self, driver):
        self.driver = driver

    def clickLogout(self):
        self.driver.find_element(By.XPATH, self.logout_click_xpath).click()
        self.driver.find_element(By.XPATH, self.button_logout_xpath).click()
