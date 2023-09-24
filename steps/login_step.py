from behave import *

@given('I am on the login page')
def step_impl(context):
    context.login.open_login_page()

@when('I enter my username "{username}"')
def step_impl(context, username):
    context.login.set_username(username)

@when('I enter my password "{password}"')
def step_impl(context, password):
    context.login.set_password(password)

@when('I click the login button')
def step_impl(context):
    context.login.click_login_btn()

@then('I am logged into the app')
def step_impl(context):
    context.login.verify_successful_login()

@then('I receive the error message "{error_msg}"')
def step_impl(context, error_msg):
    context.login.verify_failed_login(error_msg)
