from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class RegisterPage(BaseAction):
    #跳转到登录页面的按钮
    login_button = By.XPATH,'//*[text='']'
    def click_register(self):
        pass
