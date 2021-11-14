from selenium.webdriver.common.by import By


class LoginLocator(object):
    ACTION_BUTTON = (By.XPATH, '//*[@id="action-button"]')
    GO_TO_WEB = (By.XPATH, '//*[@id="fallback_block"]/div/div/a')


class ChatPageLocator(object):
    # Chat
    MESSAGE_BOX = (By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]')
    ITEM_LOC = 'div.y8WcF > div:last-child > div > div > div > div._1beEj > div > div > span'
    # Logout
    MENU_ICON_XPATH = (By.XPATH, '//*[@id="side"]/header/div[2]/div/span/div[3]')
    LOGOUT_XPATH = (By.XPATH, '//*[@id="side"]/header/div[2]/div/span/div[3]/span/div[1]/ul/li[4]/div[1]')
