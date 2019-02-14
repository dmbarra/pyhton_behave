from behave import given

from support.load_config import settings
from pages.login_page import LoginPage
from support.project_driver import ProjectDriver


@given(u'I open the page')
def open_page(context):
    project_driver = ProjectDriver()
    project_driver.load_website(settings['url'])
    context.browser = project_driver.driver


@given(u'I login on app')
def open_page(context):
    login = LoginPage(context)
    login.set_email_field(settings['email'])
    login.set_password_field(settings['password'])
    login.click_submit()

