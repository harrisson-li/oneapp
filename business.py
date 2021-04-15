from login_page import LoginPage
from init import instance
import time
from appium.webdriver.common.touch_action import TouchAction


WAITING_TIME = 10


def page():
    return LoginPage(instance.driver)


def login(username, password):
    actions = TouchAction(page().driver)
    actions.tap(page().debug_login_link())
    actions.perform()

    # page().debug_login_link().click()

    page().debug_username_input_box().send_keys(username)
    page().debug_password_input_box().send_keys(password)
    # page().debug_login_button().click()

    actions.tap(page().debug_login_button())
    actions.perform()

    # page().wait_for_activity('com.ef.core.engage.ui.screens.activity.OnBoardingActivity', WAITING_TIME)
    # time.sleep(10)
    # print(page().get_element('//android.widget.RelativeLayout/android.widget.TextView[2]').text)
    page().wait_for_text('//android.widget.RelativeLayout/android.widget.TextView[2]', '10 fundamental classes in 90 days.')
    # print(page().get_element('//android.widget.RelativeLayout/android.widget.TextView[2]').text)
    # time.sleep(10)
    page().driver.swipe(900, 1200, 200, 1200)
    page().wait_for_text('//android.widget.RelativeLayout/android.widget.TextView[2]',
                         'Online preview and review for each class.')
    # time.sleep(10)
    page().driver.swipe(900, 1200, 200, 1200)
    page().wait_for_text('//android.widget.RelativeLayout/android.widget.TextView[2]',
                         'Improve your English in 3 dimensions.')

    page().get_element('//androidx.viewpager.widget.ViewPager/android.widget.RelativeLayout/android.widget.Button').click()
    time.sleep(10)

