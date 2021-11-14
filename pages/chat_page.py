from pages.base_page import BasePage
from utils.locators import ChatPageLocator


class ChatPage(BasePage):
    def __init__(self, driver):
        self.locator = ChatPageLocator
        super().__init__(driver)

    def message_sent(self):
        pass

    def successful_send_message(self):
        pass

    def message_seen_status(self):
        pass

    def whatsapp_logout_status(self):
        pass
