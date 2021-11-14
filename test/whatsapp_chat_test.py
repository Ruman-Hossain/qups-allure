from pages.chat_page import ChatPage
from pages.search_number import SearchNumber
from test.base_test import BaseTest
from utils.test_cases import test_cases


class WhatsAppChatTest (BaseTest):
    def test_number_search(self):
        pass
        # print("\n" + str(test_cases(0)))
        # page = SearchNumber(self.driver)
        # search_result = page.search_number('+8801750519919')
        # self.assertTrue(page.check_page_loaded())

    def test_send_message(self):
        print("\n" + str(test_cases(1)))
        page = ChatPage(self.driver)
        message_sent = page.message_sent()
        self.assertIn("Yes", message_sent)

    def test_successful_send_message(self):
        print("\n" + str(test_cases(1)))
        page = ChatPage(self.driver)
        successful_status = page.successful_send_message()
        self.assertIn("Yes", successful_status)

    def test_message_seen_status(self):
        print("\n" + str(test_cases(1)))
        page = ChatPage(self.driver)
        message_seen = page.message_seen_status()
        self.assertIn("Seen", message_seen)

    def test_logout_status(self):
        print("\n" + str(test_cases(1)))
        page = ChatPage(self.driver)
        logout_status = page.whatsapp_logout_status()
        self.assertIn("Yes", logout_status)