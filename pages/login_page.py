from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LoginPage(BasePage):

    locator_dictionary = {
        "email": (By.ID, 'user_email'),
        "password": (By.ID, 'user_password'),
        "signin_button": (By.CSS_SELECTOR, "input[type='submit']")
    }

    def set_email_field(self, email):
        self.find_element(*self.locator_dictionary['email']).send_keys(email)

    def set_password_field(self, password):
        self.find_element(*self.locator_dictionary['password']).send_keys(password)

    def click_submit(self):
        self.find_element(*self.locator_dictionary['signin_button']).click()
