from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class ManagePage(BasePage):

    locator_dictionary = {
        "my_taks": (By.CSS_SELECTOR, ".nav a[href='/tasks']"),
        "success_message": (By.CLASS_NAME, 'alert alert-info'),
        "welcome_message": (By.CSS_SELECTOR, "h1"),
        "add_task": (By.CSS_SELECTOR, "span[class='input-group-addon glyphicon glyphicon-plus']")
    }

    def click_my_tasks(self):
        self.find_element(*self.locator_dictionary['my_taks']).click()

    def return_message_alert(self):
        return self.find_element(*self.locator_dictionary['success_message']).text

    def my_task_is_present(self):
        return self.find_element(*self.locator_dictionary['my_taks']).size['width'] > 0

    def return_message_welcome(self):
        return self.find_element(*self.locator_dictionary['welcome_message']).text

    def add_task_is_present(self):
        return self.find_element(*self.locator_dictionary['add_task']).size['width'] > 0

    def add_my_tasks(self):
        self.find_element(*self.locator_dictionary['add_task']).click()
