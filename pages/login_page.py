from pages.base_page import BasePage
from utils.locators import *


class login_page(BasePage):
    def __init__(self):
        self.locator = LoginLocator
        super().__init__(self.driver)

