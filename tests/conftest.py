import inspect

import pytest
from selenium import webdriver
from utils.config_loader import load_config

@pytest.fixture(scope="class")
def setup_driver(request):
    # Get environment from command line
    env = request.config.getoption("--env")
    config = load_config(env)

    # Get Browser from command line
    browser = request.config.getoption("--browser")

    # Setup WebDriver
    if browser == 'chrome':
        driver = webdriver.Chrome()
    elif browser == 'firefox':
        driver = webdriver.Firefox()
    driver.implicitly_wait(10)
    driver.maximize_window()

    # Attach driver and config to request object for access in tests
    request.cls.driver = driver
    request.cls.config = config

    yield

    # Teardown
    driver.quit()
    print("Test Completed")

def pytest_addoption(parser):
    parser.addoption("--env", action="store", default="dev", help="Environment to run tests against")
    parser.addoption("--browser", action="store", default="chrome", help="Environment to run tests against")
