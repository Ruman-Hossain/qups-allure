import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import Keys
from pages.base_page import BasePage
from utils.locators import ChatPageLocator


# Processing Functions
def message_sent_or_pending(label):
    if label == 'Sent':
        return 'Yes'
    elif label == 'Delivered':
        return 'Yes'
    elif label == 'Read':
        return 'Yes'
    elif label == 'Pending':
        return 'No'


def message_seen_or_not(label):
    if label == 'Sent':
        return 'Not Seen'
    elif label == 'Delivered':
        return 'Not Seen'
    elif label == 'Read':
        return 'Seen'
    elif label == 'Pending':
        return 'Not Seen'


class ChatPage(BasePage):
    def __init__(self, driver):
        self.locator = ChatPageLocator
        super().__init__(driver)

    def message_sent(self, message):
        self.find_element(*self.locator.MESSAGE_BOX).send_keys(message + Keys.ENTER)
        time.sleep(2)

    def successful_send_message(self, message):
        self.message_sent(message)
        value = self.find_element(*self.locator.ITEM_LOC).get_attribute('area-label')
        label = ''.join(value.split())
        return message_sent_or_pending(label)

    def message_seen_status(self, message):
        self.message_sent(message)
        value = self.find_element(*self.locator.ITEM_LOC).get_attribute('area-label')
        label = ''.join(value.split())
        return message_seen_or_not(label)

    def whatsapp_logout_status(self):
        try:
            self.wait_element(*self.locator.MENU_ICON_XPATH).click()
            time.sleep(2)
            self.wait_element(*self.locator.LOGOUT_XPATH).click()
            return 'Yes'
        except (NoSuchElementException, Exception) as ec:
            print(ec)
            return 'No'
