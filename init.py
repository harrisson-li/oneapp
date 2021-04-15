import unittest
from appium import webdriver
from appium.webdriver.appium_service import AppiumService
import os
import pytest
from data import *


class Container:
    service = None
    driver = None


instance = Container()


class TestBase:

    def setup_class(self):
        # service = AppiumService()
        # service.start(args=['--address', '127.0.0.1', '-p', '4724'])
        #
        # instance.service = service
        #
        # os.system(
        #     '/Applications/Genymotion.app/Contents/MacOS/player.app/Contents/MacOS/player --vm-name "Huawei P30 Pro"')

        app = android_app

        desired_caps = {}
        # desired_caps['app'] = app
        desired_caps['platformName'] = 'Android'
        desired_caps['platfromVersion'] = '9.0'
        desired_caps['deviceName'] = 'Huawei P30 Pro'
        desired_caps['orientation'] = 'LANDSCAPE'  # LANDSCAPE or PORTRAIT

        self.driver = webdriver.Remote(command_executor='http://127.0.0.1:4724/wd/hub',
                                       desired_capabilities=desired_caps)

        instance.driver = self.driver

    def teardown_class(self):
        instance.driver.quit()
        # instance.service.stop()
        # os.system('killall -9 player')


@pytest.fixture()
def setup_teardown_android():
    app = android_app

    desired_caps = {}
    desired_caps['app'] = app
    desired_caps['platformName'] = 'Android'
    desired_caps['platfromVersion'] = '9.0'
    desired_caps['deviceName'] = 'Huawei P30 Pro'
    desired_caps['fullReset'] = True

    driver = webdriver.Remote(command_executor='http://127.0.0.1:4724/wd/hub',
                              desired_capabilities=desired_caps)
    instance.driver = driver
    yield
    instance.driver.quit()


@pytest.fixture()
def setup_teardown_ios():
    app = ios_app

    desired_caps = {}
    desired_caps['app'] = app
    desired_caps['platformName'] = 'iOS'
    desired_caps['platfromVersion'] = '14.4'
    desired_caps['deviceName'] = 'iPhone 11 Pro'
    desired_caps["automationName"] = "XCUITest"
    # desired_caps['orientation'] = 'LANDSCAPE'  # LANDSCAPE or PORTRAIT
    desired_caps['fullReset'] = True

    driver = webdriver.Remote(command_executor='http://127.0.0.1:4724/wd/hub',
                              desired_capabilities=desired_caps)
    instance.driver = driver
    yield
    instance.driver.quit()
