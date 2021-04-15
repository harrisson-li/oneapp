from init import *
from business import login
import pytest
import time
from install import install_app, launch_app
from data import *


class TestOneApp():

    def atest_login(self):
        login('stestc85725', '1')

    @pytest.mark.usefixtures('setup_teardown_android')
    def atest_install(self):
        # install_app(android_bundle_name, android_app)
        launch_app(android_bundle_name)
        # time.sleep(100)

    # @pytest.mark.usefixtures('setup_teardown_android')
    @pytest.mark.usefixtures('setup_teardown_ios')
    def test_func(self):
        time.sleep(10)


if __name__ == '__main__':
    pytest.main(['-rA'])
