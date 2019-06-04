
from base.base_driver import BaseDriver
from page.page import Page


class TestLogin:

    def setup(self):
        self.driver = BaseDriver.init_driver()
        self.page = Page(self.driver)

    def test_login(self):
        pass