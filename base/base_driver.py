from appium.webdriver import webdriver


class BaseDriver:

    def init_driver(self):
        desired_caps = dict()
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.1'
        desired_caps['deviceName'] = '192.168.56.101:5555'
        desired_caps['appPackage'] = 'com.yunmall.lc'
        desired_caps['appActivity'] = 'com.yunmall.ymctoc.ui.activity.LogonActivity'
        desired_caps['noReset'] = True

        return webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)