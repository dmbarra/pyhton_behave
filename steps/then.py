from behave import then


@then(u'I see "My Tasks"')
def verify_my_task_link(context):
    pass


@then(u'I see message saying that list belongs to that user')
def verify_message_about_user(context):
    pass


@then(u'I can create new task')
def verify_possibility_create_new_task(context):
    pass
