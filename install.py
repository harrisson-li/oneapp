from init import instance
from data import app_status
import time


def check_app_status(status_code):
    print(app_status[str(status_code)])


def install_app(bundle_name, app_file):
    driver = instance.driver

    if driver.is_app_installed(bundle_name):
        driver.remove_app(bundle_name)

    driver.install_app(app_file)
    check_app_status(driver.query_app_state(bundle_name))

    driver.activate_app(bundle_name)
    time.sleep(10)
    check_app_status(driver.query_app_state(bundle_name))

    driver.background_app(-1)
    check_app_status(driver.query_app_state(bundle_name))
    time.sleep(3)

    driver.activate_app(bundle_name)
    time.sleep(10)
    check_app_status(driver.query_app_state(bundle_name))

    driver.terminate_app(bundle_name)
    time.sleep(3)
    check_app_status(driver.query_app_state(bundle_name))


def launch_app(bundle_name):
    driver = instance.driver

    time.sleep(10)
    driver.close_app()
    check_app_status(driver.query_app_state(bundle_name))

    driver.launch_app()
    time.sleep(10)
    check_app_status(driver.query_app_state(bundle_name))

    driver.reset()
    time.sleep(10)
    check_app_status(driver.query_app_state(bundle_name))
