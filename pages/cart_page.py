from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from browser import Browser


class Cart(Browser):

    ITEMS_NAMES = (By.XPATH, '//div[@class="inventory_item_name"]')
    REMOVE_BTN = (By.XPATH, '//button[text()="Remove"]')

    def remove_item_from_cart(self):
        self.driver.find_element(*self.REMOVE_BTN).click()

    def verify_item_in_cart(self, item):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.presence_of_element_located(self.ITEMS_NAMES))

        print(self.driver.page_source)

        item_on_page = element.text

        assert item == item_on_page, (f"Error: We added the item {item} to the cart, "
                                      f"but we found the item {item_on_page} in the cart.")

