import time

from selenium.webdriver.common.by import By

from browser import Browser


class Inventory(Browser):
    ITEM_NAME = (By.XPATH, '//div[@class="inventory_item_name"]')
    CART_BTN = (By.CSS_SELECTOR, "a.shopping_cart_link")
    ITEMS_CART = (By.XPATH, '//span[@class="shopping_cart_badge"]')

    items_dict = {
        "Sauce Labs Backpack" : "add-to-cart-sauce-labs-backpack",
        "Sauce Labs Bolt T-Shirt" : "add-to-cart-sauce-labs-bolt-t-shirt",
        "Sauce Labs Onesie" : "add-to-cart-sauce-labs-onesie",
        "Sauce Labs Bike Light" : "add-to-cart-sauce-labs-bike-light",
        "Sauce Labs Fleece Jacket" : "add-to-cart-sauce-labs-fleece-jacket",
        "Test.allTheThings() T-Shirt (Red)" : "add-to-cart-test.allthethings()-t-shirt-(red)"
    }

    def click_add_toCart_item(self, item):
        for item_in_dict in self.items_dict:
            if item == item_in_dict:
                self.driver.find_element(By.ID, self.items_dict[item_in_dict]).click()
                print(self.items_dict[item_in_dict])
                time.sleep(2)

    def add_to_cart_items(self, items_nr):
        items_ids = list(self.items_dict.values())
        print(items_ids)
        for i in range(items_nr):
            self.driver.find_element(By.ID, items_ids[i]).click()

    def click_cart_btn(self):
        self.driver.find_element(*self.CART_BTN).click()

    def verify_no_of_items_in_cart(self, no_of_items):
        items_in_cart = self.driver.find_element(*self.ITEMS_CART).text
        assert no_of_items == int(items_in_cart), f"error: {no_of_items} is random but in cart we have {items_in_cart}"
