from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class ManageSubTaskPage(BasePage):

    locator_dictionary = {
        "subtask_name": (By.ID, "new_sub_task"),
        "subtask_date": (By.ID, "dueDate"),
        "submit_subtask": (By.ID, "add-subtask"),
        "table_of_subtasks": (By.CSS_SELECTOR, ".table tbody")
    }

    def set_subtask_name(self, name):
        self.find_element(*self.locator_dictionary['subtask_name']).send_keys(name)

    def set_subtask_date(self, date):
        self.find_element(*self.locator_dictionary['subtask_date']).send_keys(date)

    def add_subtask(self):
        self.find_element(*self.locator_dictionary['submit_subtask']).click()

    def my_subtask_is_present_on_table(self, value):
        table_id = self.find_elements(*self.locator_dictionary['table_of_subtasks'])[1]
        rows = table_id.find_elements(By.TAG_NAME, "tr")
        for row in rows:
            return row.find_elements(By.TAG_NAME, "td")[1].text == value
