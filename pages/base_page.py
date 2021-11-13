from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.base_url = 'https://web.whatsapp.com/'
        self.suffix_link = 'https://wa.me/'
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 100)
        self.number = ''
        self.message = ''
        self.read_status = ''
        self.delivered_status = ''

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def open(self, number):
        url = self.base_url + number
        self.driver.get(url)

    def get_title(self):
        return self.driver.title

    def get_url(self):
        return self.driver.current_url

    def hover(self, *locator):
        element = self.find_element(*locator)
        hover_element = ActionChains(self.driver).move_to_element(element)
        hover_element.perform()

    def wait_element(self, *locator):
        try:
            WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(locator))
        except TimeoutException:
            print("\n * ELEMENT NOT FOUND WITHIN GIVEN TIME! --> %s" % (locator[1]))
            self.driver.quit()
