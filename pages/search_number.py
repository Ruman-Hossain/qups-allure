from pages.base_page import BasePage
from utils.locators import *


class SearchNumber(BasePage):
    def __init__(self):
        self.locator = LoginLocator
        super().__init__()

    def search(self, number):
        return BasePage.open(self, number)

    def search_valid_number(self, number):
        self.search(number)

    def search_invalid_number(self, number):
        self.search(number)
        return


        