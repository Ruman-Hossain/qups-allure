from selenium.webdriver.common.by import By


class SearchNumberLocator(object):
    ACTION_BUTTON = (By.XPATH, '//*[@id="action-button"]')
    GO_TO_WEB = (By.XPATH, '//*[@id="fallback_block"]/div/div/a')


class SendMessageLocator(object):
    MESSAGE_BOX = (By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]')


class LogoutLocator(object):
    MENU_ICON = (By.XPATH, '//*[@id="side"]/header/div[2]/div/span/div[3]')
    LOGOUT = (By.XPATH, '//*[@id="side"]/header/div[2]/div/span/div[3]/span/div[1]/ul/li[5]')
