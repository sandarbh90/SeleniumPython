from selenium.webdriver.common.by import By


class LoginPage():
    def __init__(self,driver):
        self.driver = driver
        self.username_textbox ="//input[@name='username']"
        self.password_textbox="//input[@name='password']"
        self.login_button="//button[contains(@class, 'orangehrm-login-button')]"

    def enterUsername(self,username):
        self.driver.find_element(By.XPATH, self.username_textbox).send_keys(username)

    def enterPassword(self,password):
        self.driver.find_element(By.XPATH, self.password_textbox).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.XPATH, self.login_button).click()

