from selenium import webdriver

class InventoryPage(object):

    def __init__(self, selenium):
        self.driver = selenium

    def add_item_to_cart(self):
        self.driver.find_element_by_css_selector('.btn_primary').click()

    def remove_item_from_cart(self):
        self.driver.find_element_by_css_selector('.btn_secondary').click()

    def get_items_in_cart(self):
        return self.driver.find_element_by_css_selector('.shopping_cart_badge').text

    def get_current_url(self):
        return self.driver.current_url

    def visit(self):
        self.driver.get('https://www.saucedemo.com/inventory.html')