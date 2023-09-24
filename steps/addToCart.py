from behave import *


@given('I am logged into the app')
def step_impl(context):
    context.login.login_into_app()


@when('I click add to cart button for the item "{item}"')
def step_impl(context, item):
    context.inventory.click_add_tocart_item(item)


@when('I click on the cart button')
def step_impl(context):
    context.inventory.click_cart_btn()


@then('I check that the item "{item}" was added to the cart')
def step_impl(context, item):
    context.cart.verify_item_in_cart(item)
    context.cart.remove_item_from_cart()
