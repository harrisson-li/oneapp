import unittest
from appium import webdriver
from appium.webdriver.appium_service import AppiumService
import os


class Container:
    service = None
    driver = None


instance = Container()


class TestBase(unittest.TestCase):

    def setUp(self):
        # service = AppiumService()
        # service.start(args=['--address', '127.0.0.1', '-p', '4724'])
        #
        # instance.service = service
        #
        # os.system(
        #     '/Applications/Genymotion.app/Contents/MacOS/player.app/Contents/MacOS/player --vm-name "Huawei P30 Pro"')

        app = os.path.abspath('/Users/lizhichao/Downloads/ec.apk')

        desired_caps = {}
        desired_caps['app'] = app
        desired_caps['platformName'] = 'Android'
        desired_caps['platfromVersion'] = '9.0'
        desired_caps['deviceName'] = 'Huawei P30 Pro'

        self.driver = webdriver.Remote(command_executor='http://127.0.0.1:4724/wd/hub',
                                       desired_capabilities=desired_caps)

        instance.driver = self.driver

    def tearDown(self):
        instance.driver.quit()
        # instance.service.stop()
        # os.system('killall -9 player')

