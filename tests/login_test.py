import os

import allure
import moment
import pytest
from pages.loginPage import LoginPage
from pages.homePage import HomePage
from utils.helper import Helper


@pytest.mark.usefixtures("setup_driver")
class TestLogin:

    def test_login(self):
        self.driver.get(self.config["base_url"])
        login = LoginPage(self.driver)
        login.enterUsername(self.config["username"])
        login.enterPassword(self.config["password"])
        login.click_login()


    def test_logout(self):
        try:
            homePage = HomePage(self.driver)
            homePage.open_user_dropdown()
            homePage.click_logout()
            page_title = self.driver.title
            assert page_title=="OrangeHRM"
        except AssertionError as error:
            print(error)
            print("Assertion error Occurred")
            allure.attach(self.driver.get_screenshot_as_png(),name="Screenshot_"+Helper.whoami()+"_"+str(moment.now()),attachment_type=allure.attachment_type.PNG)
            # Get the path to the parent directory (project root)
            project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            print(f"project_root---{project_root}")
            screenshots_dir = os.path.join(project_root, "screenshots")
            print(f"screenshots_dir---- {screenshots_dir}")
            filename = f"Screenshot_{Helper.whoami()}_{str(moment.now())}.png"
            filepath = os.path.join(screenshots_dir, filename)
            self.driver.get_screenshot_as_file(filepath)
      #      self.driver.get_screenshot_as_file("../screenshots/"+"Screenshot_"+Helper.whoami()+"_"+str(moment.now())+".png")
            raise
        except:
            print("There was an exception")
            raise
        else:
            print("No exception raised in try block")
        finally:
            print("in finally block")
