import time

from selenium.webdriver.common.by import By

from browser import Browser


class Inventory(Browser):
    ITEM_NAME = (By.XPATH, '//div[@class="inventory_item_name"]')
    CART_BTN = (By.XPATH, '//a[@class="shopping_cart_link"]')

    items_dict = {
        "Sauce Labs Backpack" : "add-to-cart-sauce-labs-backpack",
        "Sauce Labs Bolt T-Shirt" : "add-to-cart-sauce-labs-bolt-t-shirt",
        "Sauce Labs Onesie" : "add-to-cart-sauce-labs-onesie",
        "Sauce Labs Bike Light" : "add-to-cart-sauce-labs-bike-light",
        "Sauce Labs Fleece Jacket" : "add-to-cart-sauce-labs-fleece-jacket",
        "Test.allTheThings() T-Shirt (Red)": "add-to-cart-test.allthethings()-t-shirt-(red)"
        }

    def click_add_tocart_item(self, item):
        for item_in_dict in self.items_dict:
            if item == item_in_dict:
                self.driver.find_element(By.ID, self.items_dict[item_in_dict]).click()


    def click_cart_btn(self):
        self.driver.find_element(*self.CART_BTN).click()
