import random

from behave import when

from pages.manage_subtask_page import ManageSubTaskPage
from pages.manage_task_page import ManageTaskPage


@when(u'I add new task')
def open_page(context):
    manage = ManageTaskPage(context)
    manage.click_my_tasks()
    context.task_name = str("Daniel " + str(random.randint(1,1000)))
    manage.set_task_name(context.task_name)
    manage.click_add_tasks()


@when(u'I fill subtask description')
def fill_description(context):
    manage_subtask = ManageSubTaskPage(context)
    context.subtask_name = str("Daniel subtask " + str(random.randint(1, 1000)))
    manage_subtask.set_subtask_name(context.subtask_name)


@when(u'I fill the subtask date')
def fill_date(context):
    manage_subtask = ManageSubTaskPage(context)
    manage_subtask.set_subtask_date("02/17/2019")


@when(u'I submit subtask')
def submit_subtasks(context):
    manage_subtask = ManageSubTaskPage(context)
    manage_subtask.add_subtask()

