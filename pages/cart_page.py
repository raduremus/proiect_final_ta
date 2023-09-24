from selenium.webdriver.common.by import By

from browser import Browser


class Cart(Browser):

    ITEMS_NAMES = (By.XPATH, '//div[@class="inventory_item_name"]')
    REMOVE_BTN = (By.XPATH, '//button[text()="Remove"]')

    def remove_item_from_cart(self):
        self.driver.find_element(*self.REMOVE_BTN).click()

    def verify_item_in_cart(self, item):
        item_on_page = self.driver.find_element(*self.ITEMS_NAMES).text
        assert item == item_on_page, (f"Error: We added to cart the item {item} "
                                      f"but in cart we found the item {item_on_page}")
