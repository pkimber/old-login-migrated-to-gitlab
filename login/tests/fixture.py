# -*- encoding: utf-8 -*-
import pytest

from login.tests.factories import (
    TEST_PASSWORD,
    UserFactory,
)


class PermTest:

    def __init__(self, client):
        setup_users()
        self.client = client

    def anon(self, url):
        self.client.logout()
        response = self.client.get(url)
        message = "'url should be public '{}'".format(url)
        assert 200 == response.status_code, message

    def staff(self, url):
        # check anon user cannot login
        self.client.logout()
        response = self.client.get(url)
        assert 302 == response.status_code
        assert 'accounts/login' in response['Location']
        # check web user cannot login
        assert self.client.login(username='web', password=TEST_PASSWORD)
        assert 302 == response.status_code
        assert 'accounts/login' in response['Location']
        # check staff user can login
        assert self.client.login(username='staff', password=TEST_PASSWORD)
        response = self.client.get(url)
        assert 200 == response.status_code


@pytest.fixture
def perm_check(client):
    """Check permissions on a URL.

    We use a clever trick to pass parameters to the fixture.  For details:
    py.test: Pass a parameter to a fixture function
    http://stackoverflow.com/questions/18011902/py-test-pass-a-parameter-to-a-fixture-function

    """
    return PermTest(client)


def setup_users():
    """Using factories - set-up users for permissions test cases."""
    UserFactory(
        username='admin',
        email='admin@pkimber.net',
        is_staff=True,
        is_superuser=True
    )
    UserFactory(username='staff', email='staff@pkimber.net', is_staff=True)
    UserFactory(
        username='web', email='web@pkimber.net',
        first_name='William', last_name='Webber'
    )
