import time

from selenium import webdriver
import allure
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import (
    UnexpectedAlertPresentException,
    NoSuchElementException,
)
from selenium.webdriver.support.wait import WebDriverWait


@allure.severity(allure.severity_level.NORMAL)
class WhatsAppUi:
    @allure.severity(allure.severity_level.MINOR)
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.BASE_URL = 'https://web.whatsapp.com/'
        self.SUFFIX_LINK = 'https://wa.me/'
        self.driver.get(self.BASE_URL)
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 100)
        self.number = ''
        self.message = ''
        self.read_status = ''
        self.delivered_status = ''

    @allure.severity(allure.severity_level.MINOR)
    def search_number(self, number) -> None:
        try:
            self.number = number
            phone_link = f'{self.SUFFIX_LINK}{number}'
            self.driver.get(phone_link)
            time.sleep(1)
            action_button = self.wait.until(ec.presence_of_element_located(
                (By.XPATH, '//*[@id="action-button"]')))
            action_button.click()
            time.sleep(2)
            go_to_web = self.wait.until(ec.presence_of_element_located(
                (By.XPATH, '//*[@id="fallback_block"]/div/div/a')))
            go_to_web.click()
            time.sleep(1)
        except UnexpectedAlertPresentException as bug:
            print(bug)
            time.sleep(1)
            self.search_number(number)

    @allure.severity(allure.severity_level.MINOR)
    def send_message(self, message):
        try:
            self.message = message
            msg_box_xpath = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]'
            msg_box = self.wait.until(ec.
                                      presence_of_element_located((By.XPATH, msg_box_xpath)))
            msg_box.send_keys(message)
            msg_box.send_keys(Keys.ENTER)
            time.sleep(10)
            print(f'Message Send Successful to {self.number}')
        except (NoSuchElementException, Exception) as bug:
            print(bug)
            print(f'Failed to send message to {self.number} ')
        finally:
            print('Send Message() Finished Running.')

    @allure.severity(allure.severity_level.MINOR)
    def verify_successfully_send_message(self):
        try:
            self.driver.find_element(By.CLASS_NAME, 'kOrB_').click()
            read_class = self.driver.find_element(By.CLASS_NAME, 'YYcY9')
            read_color = read_class.value_of_css_property('color')
            try:
                if read_color == 'var(--icon-ack)':
                    self.read_status = 'Yes'
                    print(f"Read Status Checking Successful : {self.read_status}")
                else:
                    self.read_status = 'No'
            except (NoSuchElementException, Exception) as bug:
                print(bug)
                print('Read Status Checking Failed')

            delivered_class = self.driver.find_element(By.CLASS_NAME, '')
            delivered_color = delivered_class.value_of_css_property('color')
            try:
                if delivered_color == "var(--icon-lighter)":
                    self.delivered_status = 'Yes'
                    print("Delivered Status Checking Successful : {delivered_status}")
            except (NoSuchElementException, Exception) as bug:
                print(bug)
                print('Delivered Status Checking Failed')
        except (NoSuchElementException, Exception) as bug:
            print(bug)

    @allure.severity(allure.severity_level.MINOR)
    def send_message_status(self):
        pass

    @allure.severity(allure.severity_level.MINOR)
    def verify_logout(self):
        pass
        # try:
        #     menu_xpath = '//*[@id="side"]/header/div[2]/div/span/div[3]'
        #     self.wait.until(ec.presence_of_element_located((By.XPATH, menu_xpath))).click()
        #     logout_xpath = '//*[@id="side"]/header/div[2]/div/span/div[3]/span/div[1]/ul/li[5]'
        #     self.wait.until(ec.presence_of_element_located((By.XPATH, logout_xpath))).click()
        #     print("Log Out Action Done Successfully.")
        # except (NoSuchElementException, Exception) as bug:
        #     print(bug)
        #     self.verify_logout()
