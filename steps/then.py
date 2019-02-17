from behave import then
import verify

from pages.manage_subtask_page import ManageSubTaskPage
from pages.manage_task_page import ManageTaskPage


@then(u'I see "My Tasks"')
def verify_my_task_link(context):
    manage = ManageTaskPage(context)
    verify.Truthy(manage.my_task_is_present())
    manage.click_my_tasks()


@then(u'I see message saying that list belongs to that user')
def verify_message_about_user(context):
    manage = ManageTaskPage(context)
    verify.Equal(manage.return_message_welcome(), "​Hey Daniel Barra, this is your todo list for today:")


@then(u'I can create new task')
def verify_possibility_create_new_task(context):
    manage = ManageTaskPage(context)
    verify.Truthy(manage.add_task_is_present())
    manage.click_add_tasks()


@then(u'the new task is present on list')
def verify_new_task_table(context):
    manage = ManageTaskPage(context)
    verify.Truthy(manage.my_task_is_present_on_table(context.task_name))


@then(u'the new subtask is present on list of subtasks')
def verify_new_sub_task_table(context):
    manage_subtask = ManageSubTaskPage(context)
    verify.Truthy(manage_subtask.my_subtask_is_present_on_table(context.subtask_name))


@then(u'the numbers of subtasks is showed on tasks table')
def verify_numbers_of_subtask_table(context):
    manage = ManageTaskPage(context)
    verify.Equal(manage.how_many_subtasks(context.task_name), 1)


@then(u'numbers of subtasks is zero')
def verify_numbers_of_subtask_table(context):
    manage = ManageTaskPage(context)
    verify.Equal(manage.how_many_subtasks(context.task_name), 0)
