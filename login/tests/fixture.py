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

    def _no_login_anon(self, url):
        """Check anon user cannot login."""
        self.client.logout()
        response = self.client.get(url)
        assert response.status_code in [302, 401]
        if response.status_code == 302:
            assert '/login' in response['Location']

    def _no_login_staff(self, url):
        """Check staff user cannot login."""
        assert self.client.login(username='staff', password=TEST_PASSWORD)
        response = self.client.get(url)
        assert 302 == response.status_code
        assert '/login' in response['Location']

    def _no_login_web(self, url):
        """Check web user cannot login."""
        assert self.client.login(username='web', password=TEST_PASSWORD)
        response = self.client.get(url)
        assert response.status_code in [302, 401, 403]
        if response.status_code == 302:
            assert '/login' in response['Location']

    def admin(self, url):
        self._no_login_anon(url)
        self._no_login_web(url)
        self._no_login_staff(url)
        # check staff user can login
        assert self.client.login(username='admin', password=TEST_PASSWORD)
        response = self.client.get(url)
        assert 200 == response.status_code

    def anon(self, url):
        self.client.logout()
        response = self.client.get(url)
        message = "'url should be public '{}'".format(url)
        assert 200 == response.status_code, message

    def auth(self, url, expect=None, expect_location=None):
        """Check a user who is logged in has access to the view.

        Keyword arguments:
        expect -- can be used when the expected status code is not 200.
        expect_location -- can be used where the expected status code is 302
        and we want to verify the redirect.

        """
        if not expect:
            expect = 200
        # check a user who 'is_authenticated' can login
        self.client.logout()
        response = self.client.get(url)
        assert 302 == response.status_code
        assert '/login' in response['Location']
        # check web user can login
        self.client.logout()
        assert self.client.login(username='web', password=TEST_PASSWORD)
        response = self.client.get(url)
        assert expect == response.status_code, response['Location']
        # check staff user can login
        self.client.logout()
        assert self.client.login(username='staff', password=TEST_PASSWORD)
        response = self.client.get(url)
        assert expect == response.status_code
        if expect_location:
            assert expect_location == response['Location']

    def staff(self, url):
        self._no_login_anon(url)
        self._no_login_web(url)
        # check staff user can login
        assert self.client.login(username='staff', password=TEST_PASSWORD)
        response = self.client.get(url)
        assert 200 == response.status_code, response


@pytest.fixture
def perm_check(client):
    """Check permissions on a URL.

    We use a clever trick to pass parameters to the fixture.  For details:
    py.test: Pass a parameter to a fixture function
    http://stackoverflow.com/questions/18011902/py-test-pass-a-parameter-to-a-fixture-function

    To use this fixture::

      from login.tests.fixture import perm_check

      @pytest.mark.django_db
      def test_list(perm_check):
          url = reverse('enquiry.list')
          perm_check.staff(url)

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
