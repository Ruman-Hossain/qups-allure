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
        self.read_status = 'Not Seen'
        self.delivered_status = 'No'
        self.pending_status = 'No'
        self.sent_status = 'No'
        self.login_status = 'No'
        self.logout_status = 'No'

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
            print("TC-001 : Search Number : Pass")
        except UnexpectedAlertPresentException as bug:
            print(bug)
            time.sleep(1)
            print("TC-001 : Search Number : Failed")
            self.search_number(number)
        finally:
            self.login_status = 'Yes'

    @allure.severity(allure.severity_level.MINOR)
    def send_message(self, message):
        try:
            self.message = message
            msg_box_xpath = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]'
            msg_box = self.wait.until(ec.
                                      presence_of_element_located((By.XPATH, msg_box_xpath)))
            msg_box.send_keys(message + Keys.ENTER)
            print(f"Message : {self.message}")
            time.sleep(2)
            print(f'Message Send Successful to {self.number}')
            time.sleep(10)
            print('TC-002 : Send Message : Pass')
        except (NoSuchElementException, Exception) as bug:
            print(bug)
            print('TC-002 : Send Message : Failed')
        finally:
            self.verify_successfully_send_message()

    @allure.severity(allure.severity_level.MINOR)
    def verify_successfully_send_message(self):
        try:
            # print("Verify Successfully Send Message Function Initiated")
            item_loc = "div.y8WcF > div:last-child > div > div > div > div._1beEj > div > div > span"
            item_val = self.driver.find_element(By.CSS_SELECTOR, item_loc).get_attribute('aria-label')
            item_val = ''.join(item_val.split())
            print(f"Message Status : {item_val}")
            if item_val == 'Sent':
                print('TC-003 : Successfully Send Message : Pass')
                self.sent_status = 'Yes'
            elif item_val == 'Delivered':
                print('TC-003 : Successfully Send Message : Pass')
                self.delivered_status = 'Yes'
            elif item_val == 'Pending':
                print('TC-003 : Successfully Send Message : Failed')
                self.pending_status = 'Yes'
            elif item_val == 'Read':
                print('TC-003 : Successfully Send Message : Pass')
                self.read_status = 'Seen'
        except (NoSuchElementException, Exception) as bug:
            print(bug)
            print('Message Send Not Successful')
            print('TC-003 : Successfully Send Message : Failed')
        finally:
            self.seen_message_status()

    @allure.severity(allure.severity_level.MINOR)
    def seen_message_status(self):
        try:
            item_loc = "div.y8WcF > div:last-child > div > div > div > div._1beEj > div > div > span"
            item_val = self.driver.find_element(By.CSS_SELECTOR, item_loc).get_attribute('aria-label')
            item_val = ''.join(item_val.split())
            if item_val == 'Read':
                print(f"{item_val} : Message Seen By The Receiver")
                self.read_status = 'Seen'
                print('TC-004 : Read Status : Seen')
            else:
                print('TC-004 : Read Status : Not Seen')
        except (NoSuchElementException, Exception) as bug:
            print(bug)
            print('Message Seen Checking Failed')
        finally:
            self.verify_logout()

    @allure.severity(allure.severity_level.MINOR)
    def verify_logout(self):
        try:
            menu_xpath = '//*[@id="side"]/header/div[2]/div/span/div[3]'
            self.wait.until(ec.presence_of_element_located((By.XPATH, menu_xpath))).click()
            time.sleep(2)
            logout_xpath = '//*[@id="side"]/header/div[2]/div/span/div[3]/span/div[1]/ul/li[4]/div[1]'
            self.wait.until(ec.presence_of_element_located((By.XPATH, logout_xpath))).click()
            print("Log Out Done Successfully.")
            self.logout_status = 'Yes'
            print('TC-005 : Logout : Pass')
        except (NoSuchElementException, Exception) as bug:
            print(bug)
            print("TC-005 : Logout Failed")
        finally:
            self.driver.quit()
