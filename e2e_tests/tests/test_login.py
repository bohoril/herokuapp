from e2e_tests.pages.login_page import LoginPage


def test_valid_login(page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("tomsmith", "SuperSecretPassword!")

    assert login_page.success_flash_message.is_visible()


def test_invalid_login(page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("wrong_username", "wrong_password")

    assert login_page.error_flash_message.is_visible()
