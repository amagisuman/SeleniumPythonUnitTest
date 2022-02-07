from selenium.webdriver.common.by import By


class LoginPage:
    # Locators of all elements
    textbox_username_name = "email"
    textbox_password_name = "password"
    button_login_xpath = "//*[@id='root']/div[2]/div[2]/div[2]/form/div[3]/button/span[1]"

    def __init__(self, driver):
        self.driver = driver

    def setUserName(self, username):
        self.driver.find_element(By.NAME, self.textbox_username_name).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element(By.NAME, self.textbox_password_name).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()
