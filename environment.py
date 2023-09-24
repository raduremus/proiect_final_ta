from browser import Browser
from pages.login_page import Login
from pages.inventory_page import Inventory
from pages.cart_page import Cart


def before_all(context):
    context.browser = Browser()
    context.login = Login()
    context.inventory = Inventory()
    context.cart = Cart()


def after_all(context):
    context.browser.close()
