from behave import fixture, use_fixture
from selenium import webdriver
import chromedriver_autoinstaller
import time


@fixture
def selenium_browser_chrome(context):
    chromedriver_autoinstaller.install()
    context.driver = webdriver.Chrome()
    yield context.driver
    context.driver.quit()


def before_all(context):
    use_fixture(selenium_browser_chrome, context)
