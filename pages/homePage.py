from selenium.webdriver.common.by import By


class HomePage():
    def __init__(self,driver):
        self.driver = driver
        self.user_dropdown="//li[contains(@class,'oxd-userdropdown')]"
        self.logout="Logout"

    def open_user_dropdown(self):
        self.driver.find_element(By.XPATH, self.user_dropdown).click()

    def click_logout(self):
        self.driver.find_element(By.LINK_TEXT, self.logout).click()