import random

from behave import given

from pages.manage_task_page import ManageTaskPage
from support.load_config import settings
from pages.login_page import LoginPage
from support.project_driver import ProjectDriver


@given(u'I open the page')
def open_page(context):
    project_driver = ProjectDriver()
    project_driver.load_website(settings['url'])
    context.browser = project_driver.driver


@given(u'I login on app')
def login(context):
    login = LoginPage(context)
    login.set_email_field(settings['email'])
    login.set_password_field(settings['password'])
    login.click_submit()


@given(u'I have task')
def create_task(context):
    manage = ManageTaskPage(context)
    manage.click_my_tasks()
    context.task_name = str("Daniel " + str(random.randint(1,1000)))
    manage.set_task_name(context.task_name)
    manage.click_add_tasks()


@given(u'I open manage subtask')
def open_subtasks(context):
    manage = ManageTaskPage(context)
    manage.open_manage_subtasks(context.task_name)
