from pages.base_page import BasePage
from utils.locators import *


class search_page(BasePage):
    def __init__(self, driver):
        self.locator = SearchNumberLocator
        super().__init__(driver)


