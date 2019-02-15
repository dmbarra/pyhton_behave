from behave import then
import verify
from pages.manage_page import ManagePage


@then(u'I see "My Tasks"')
def verify_my_task_link(context):
    manage = ManagePage(context)
    verify.Truthy(manage.my_task_is_present())
    manage.click_my_tasks()


@then(u'I see message saying that list belongs to that user')
def verify_message_about_user(context):
    manage = ManagePage(context)
    verify.Equal(manage.return_message_welcome(), "​Hey Daniel Barra, this is your todo list for today:")


@then(u'I can create new task')
def verify_possibility_create_new_task(context):
    manage = ManagePage(context)
    verify.Truthy(manage.add_task_is_present())
    manage.click_add_tasks()


@then(u'the new task is present on list')
def verify_possibility_create_new_task(context):
    manage = ManagePage(context)
    verify.Truthy(manage.my_task_is_present_on_table(context.task_name))
