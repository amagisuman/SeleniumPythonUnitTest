import time
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class Overview:
    # Customer Selection
    click_customer_xpath = "//*[@id='root']/header/div/button/span[1]"
    select_customer_xpath = "/html/body/div[2]/div[3]/div[2]/li[7]/div/div"

    # Daily Data Interval Selection and select Last 30 Days
    click_Last7Days_xpath = "//*[@id='demo-simple-select']"
    select_Last30Days_xpath = "//*[@id='menu-range']/div[3]/ul/li[2]"
    # select_Last30Days_xpath = "//*[@id='demo-simple-select']"

    # Channel Selection
    click_OnChannel_xpath = "//*[@id='root']/div/main/div[1]/div[3]/div[2]/div[1]/div[1]/button/span"
    select_SecondChannel_xpath = "/html/body/div[2]/div[3]/div[2]/li[6]/div/div/span"

    # Daily Selection
    # Click on Unique Viewer Tab
    click_UniqueViewer_xpath = "//*[@id='root']/div/main/div[5]/div[4]/div[1]/button[2]/span[1]"
    # Click on Viewership Minutes Tab
    click_ViewershipMin_xpath = "//*[@id='root']/div/main/div[5]/div[4]/div[1]/button[3]/span[1]"
    # Click on Table View
    click_Tableview_xpath = "//*[@id='root']/div/main/div[5]/div[4]/div[2]/button[2]/span[1]"

    # Regional Selection
    click_Reg_Unique_xpath = "//*[@id='root']/div/main/div[7]/div[2]/div[1]/button[2]/span[1]"
    click_Reg_VMin_xpath = "//*[@id='root']/div/main/div[7]/div[2]/div[1]/button[3]/span[1]"
    click_Reg_Table_xpath = "//*[@id='root']/div/main/div[7]/div[2]/div[2]/button[2]/span[1]"
    view_Reg_Metrics_xpath = "//*[@id='root']/div/main/div[7]/div[1]/div"

    # Content Metrics
    view_Content_Metrics_xpath = "//*[@id='root']/div/main/div[9]/div[1]/div"
    click_order_xpath = "/html/body/div/div/main/div[9]/div[2]/div/table/thead/tr/th[2]/div"
    pagination_search_xpath = "//*[@id='root']/div/main/div[9]/div[4]/p"
    click_pagination_xpath = "//*[@id='root']/div/main/div[9]/div[4]/nav/ul/li[3]/button"

    # Hourly Selection
    select_Hourly_xpath = "//*[@id='root']/div/main/div[1]/div[2]/div[1]/button[2]/span[1]"

    # Logout
    logout_click_xpath = "//*[@id='root']/header/div/div[2]/button/span[1]/span[3]"
    button_logout_xpath = "/html/body/div[2]/div[3]/li"

    def __init__(self, driver):
        self.driver = driver

    def customerSelection(self):
        self.driver.find_element(By.XPATH, self.click_customer_xpath).click()
        self.driver.find_element(By.XPATH, self.select_customer_xpath).click()

    def dataIntervalSelection(self):
        # self.select = Select(self.driver.find_element(By.XPATH, self.select_Last30Days_xpath).click())
        # self.select.select_by_visible_text("Last 30 Days")
        self.driver.find_element(By.XPATH, self.click_Last7Days_xpath).click()
        self.driver.find_element(By.XPATH, self.select_Last30Days_xpath).click()

    def filterBySelection(self):
        self.driver.find_element(By.XPATH, self.click_OnChannel_xpath).click()
        self.driver.find_element(By.XPATH, self.select_SecondChannel_xpath).click()
        time.sleep(1)

    def dailyMetricsSelection(self):
        self.driver.find_element(By.XPATH, self.click_UniqueViewer_xpath).click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.click_ViewershipMin_xpath).click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.click_Tableview_xpath).click()
        time.sleep(2)

    def regionalMetricsSelection(self):
        reg_view = self.driver.find_element(By.XPATH, self.view_Reg_Metrics_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", reg_view)
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.click_Reg_Unique_xpath).click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.click_Reg_VMin_xpath).click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.click_Reg_Table_xpath).click()
        time.sleep(2)

    def contentMetricsSelection(self):
        content_view = self.driver.find_element(By.XPATH, self.view_Content_Metrics_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", content_view)
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.click_order_xpath).click()
        time.sleep(4)
        no_of_rows = self.driver.find_element(By.XPATH, self.pagination_search_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", no_of_rows)
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.click_pagination_xpath).click()
        time.sleep(4)

    def hourlySelection(self):
        self.driver.find_element(By.XPATH, self.select_Hourly_xpath).click()

    def clickLogout(self):
        self.driver.find_element(By.XPATH, self.logout_click_xpath).click()
        self.driver.find_element(By.XPATH, self.button_logout_xpath).click()
