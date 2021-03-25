from login_page import LoginPage
from init import instance
import time


WAITING_TIME = 10


def page():
    return LoginPage(instance.driver)


def login(username, password):
    page().debug_login_link().click()

    page().debug_username_input_box().send_keys(username)
    page().debug_password_input_box().send_keys(password)
    page().debug_login_button().click()

    page().wait_for_activity('com.ef.core.engage.ui.screens.activity.OnBoardingActivity', WAITING_TIME)
