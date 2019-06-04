from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class HomePage(BaseAction):
    #
    me_button = By.XPATH , "//*[@text='我' and @resource-id='com.yunmall.ic.']"
    def click_me(self):
        pass
