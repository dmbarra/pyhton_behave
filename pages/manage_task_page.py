import re

from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class ManageTaskPage(BasePage):

    locator_dictionary = {
        "my_taks": (By.CSS_SELECTOR, ".nav a[href='/tasks']"),
        "success_message": (By.CLASS_NAME, 'alert alert-info'),
        "welcome_message": (By.CSS_SELECTOR, "h1"),
        "add_task": (By.CSS_SELECTOR, "span[class='input-group-addon glyphicon glyphicon-plus']"),
        "task_name": (By.ID, "new_task"),
        "table_of_tasks": (By.CSS_SELECTOR, ".table tbody")

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

    def click_add_tasks(self):
        self.find_element(*self.locator_dictionary['add_task']).click()

    def set_task_name(self, name):
        self.find_element(*self.locator_dictionary['task_name']).send_keys(name)

    def my_task_is_present_on_table(self, value):
        table_id = self.find_element(*self.locator_dictionary['table_of_tasks'])
        rows = table_id.find_elements(By.TAG_NAME, "tr")
        for row in rows:
            return row.find_elements(By.TAG_NAME, "td")[1].text == value

    def open_manage_subtasks(self, task_name):
        table_id = self.find_element(*self.locator_dictionary['table_of_tasks'])
        rows = table_id.find_elements(By.TAG_NAME, "tr")
        for row in rows:
            if row.find_elements(By.TAG_NAME, "td")[1].text == task_name:
                row.find_elements(By.TAG_NAME, "td")[3].click()

    def how_many_subtasks(self, task_name):
        table_id = self.find_element(*self.locator_dictionary['table_of_tasks'])
        rows = table_id.find_elements(By.TAG_NAME, "tr")
        for row in rows:
            if row.find_elements(By.TAG_NAME, "td")[1].text == task_name:
                return int(re.sub("[^0-9]", "", row.find_elements(By.TAG_NAME, "td")[3].text))
