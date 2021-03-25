from init import TestBase
from business import login
import pytest


class TestOneApp(TestBase):

    def test_login(self):
        login('stestc85725', '1')


if __name__ == '__main__':
    pytest.main(['-rA'])
