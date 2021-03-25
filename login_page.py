from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


DEFAULT_WAITING_TIME = 30


class LoginPage:
    DEBUG_LOGIN_LINK_XPATH = '//android.widget.RelativeLayout/android.widget.TextView[1]'
    DEBUG_USERNAME_INPUT_BOX_XPATH = '//android.view.View[1]/android.view.View[1]/android.widget.EditText'
    DEBUG_PASSWORD_INPUT_BOX_XPATH = '//android.view.View[1]/android.view.View[2]/android.widget.EditText'
    DEBUG_LOGIN_BUTTON_XPATH = '//android.webkit.WebView/android.view.View[1]/android.widget.Button'

    def __init__(self, driver):
        self.driver = driver

    def get_element(self, xpath, waiting_time=DEFAULT_WAITING_TIME):
        return WebDriverWait(self.driver, waiting_time).until(expected_conditions.presence_of_element_located((By.XPATH, xpath)))

    def wait_for_activity(self, activity, waiting_time=DEFAULT_WAITING_TIME):
        self.driver.wait_activity(activity, waiting_time)

    def debug_login_link(self):
        return self.get_element(self.DEBUG_LOGIN_LINK_XPATH)

    def debug_username_input_box(self):
        return self.get_element(self.DEBUG_USERNAME_INPUT_BOX_XPATH)

    def debug_password_input_box(self):
        return self.get_element(self.DEBUG_PASSWORD_INPUT_BOX_XPATH)

    def debug_login_button(self):
        return self.get_element(self.DEBUG_LOGIN_BUTTON_XPATH)
