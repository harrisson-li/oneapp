from init import TestBase
from business import login
import pytest
import time
from install import install_app, launch_app


class TestOneApp(TestBase):

    def atest_login(self):
        login('stestc85725', '1')

    def test_install(self):
        app = '/Users/lizhichao/Downloads/ec.apk'
        bundle_name = 'com.ef.core.engage.smartenglish'

        # install_app(bundle_name, app)
        launch_app(bundle_name)
        # time.sleep(100)


if __name__ == '__main__':
    pytest.main(['-rA'])
