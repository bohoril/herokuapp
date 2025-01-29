from playwright.sync_api import Page


class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username_input = page.locator("#username")
        self.password_input = page.locator("#password")
        self.login_button = page.locator("button[type='submit']")
        self.success_flash_message = page.locator("#flash.success")
        self.error_flash_message = page.locator("#flash.error")

    def navigate(self):
        self.page.goto("http://the-internet.herokuapp.com/login")

    def login(self, username, password):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()
