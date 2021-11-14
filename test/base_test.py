import unittest

from selenium import webdriver


class BaseTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://web.whatsapp.com/')

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    pass
