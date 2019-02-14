from behave import given

from pages.login_page import LoginPage
from support.project_driver import ProjectDriver


@given(u'I open the page')
def open_page(context):
    project_driver = ProjectDriver()
    project_driver.load_website('https://qa-test.avenuecode.com/users/sign_in')
    context.browser = project_driver.driver


@given(u'I login')
def open_page(context):
    login = LoginPage(context)
    login.set_email_field('email@email.com')
    login.set_password_field('password')
    login.click_submit()

