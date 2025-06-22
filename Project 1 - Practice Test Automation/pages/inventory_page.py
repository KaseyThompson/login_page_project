from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.cart_icon = (By.CLASS_NAME, "shopping_cart_link")
        self.inventory_items = (By.CLASS_NAME, "inventory_item")
        self.add_to_cart_button = (By.CLASS_NAME, "btn_inventory")

    def cart_icon_is_visible(self):
        icon = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.cart_icon)
        )
        return icon.is_displayed()

    def add_first_item_to_cart(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.inventory_items)
        )
        self.driver.find_element(*self.add_to_cart_button).click()

    def get_cart_badge_count(self):
        badge = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))
        )
        return badge.text
