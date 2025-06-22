import pytest
from pages.login_page import LoginPage

@pytest.mark.parametrize("username,password,expect_success,expected_text", [
    ("student", "Password123", True, "Log out"),
    ("wronguser", "Password123", False, "Your username is invalid!"),
    ("student", "wrongpass", False, "Your password is invalid!"),
])

def test_login_cases(driver, username, password, expect_success, expected_text):
    driver.get("https://practicetestautomation.com/practice-test-login/")

    login_page = LoginPage(driver)

    login_page.enter_username(username)
    login_page.enter_password(password)
    login_page.click_login()

    if expect_success:
        assert expected_text in driver.page_source
    else:
        error_message = login_page.get_error_message()
        assert expected_text in error_message
        