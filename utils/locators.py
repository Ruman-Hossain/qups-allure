from selenium.webdriver.common.by import By


class SearchNumberLocator(object):
    ACTION_BUTTON = (By.XPATH, '//*[@id="action-button"]')
    GO_TO_WEB = (By.XPATH, '//*[@id="fallback_block"]/div/div/a')


class SendMessageLocator(object):
    MESSAGE_BOX = (By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]')


class SeenStatusLocator(object):
    READ_CHECKER = (By.CLASS_NAME, 'YYcY9')
    DELIVERED_CHECKER = (By.CLASS_NAME, '')
    BELOW_LAST_MESSAGE = (By.CLASS_NAME, 'VjtCX')

    # area-label = Pending | Delivered | Read
    #                   Last Message
    # <span data-testid="msg-dblcheck" aria-label=" Delivered " data-icon="msg-dblcheck" class="">
    #   <svg><path></path></svg></span>
    #               Horizontal Line Below Last Message
    # <div class="VjtCX" style="height: 0px;"></div>


class LogoutLocator(object):
    MENU_ICON = (By.XPATH, '//*[@id="side"]/header/div[2]/div/span/div[3]')
    LOGOUT = (By.XPATH, '//*[@id="side"]/header/div[2]/div/span/div[3]/span/div[1]/ul/li[5]')
