import random

from behave import when

from pages.manage_page import ManagePage


@when(u'I add new task')
def open_page(context):
    manage = ManagePage(context)
    manage.click_my_tasks()
    context.task_name = str("Daniel " + str(random.randint(1,1000)))
    manage.set_task_name(context.task_name)
    manage.click_add_tasks()
