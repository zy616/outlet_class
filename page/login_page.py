from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class LoginPage(BaseAction):
    username_eddit_text = By.ID, ""
    password_edit_text = By.ID, ""
    login_button = By.ID, ""

    def input_username(self):
        pass

    def input_pwd(self):
        pass

    def login_click(self):
        pass