from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from pages.login_page import LoginPage
from selenium.common.exceptions import NoSuchElementException
import time
import pytest

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_valid_login(driver: WebDriver):
    driver.get("https://practicetestautomation.com/practice-test-login/")

    login_page = LoginPage(driver)

    login_page.enter_username("student")
    login_page.enter_password("Password123")
    login_page.click_login()

    assert "Log out" in driver.page_source

    time.sleep(2)

def test_invalid_username(driver: WebDriver):
    driver.get("https://practicetestautomation.com/practice-test-login/")

    login_page = LoginPage(driver)

    login_page.enter_username("wronguser")
    login_page.enter_password("Password123")
    login_page.click_login()

    error_message = login_page.get_error_message()
    assert "Your username is invalid!" in error_message

    time.sleep(2)

def test_invalid_password(driver: WebDriver):
    driver.get("https://practicetestautomation.com/practice-test-login/")

    login_page = LoginPage(driver)

    login_page.enter_username("student")
    login_page.enter_password("wrongpass")
    login_page.click_login()

    error_message = login_page.get_error_message()
    assert "Your password is invalid!" in error_message

    time.sleep(2)

def test_login_and_logout(driver: WebDriver):
    driver.get("https://practicetestautomation.com/practice-test-login/")

    login_page = LoginPage(driver)

    login_page.enter_username("student")
    login_page.enter_password("Password123")
    login_page.click_login()

    assert "Log out" in driver.page_source

    login_page.logout()

    assert "Username" in driver.page_source

    time.sleep(2)

