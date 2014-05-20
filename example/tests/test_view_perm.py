# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.core.urlresolvers import reverse

from base.tests.test_utils import PermTestCase
from login.tests.scenario import (
    default_scenario_login,
    get_user_web,
)


class TestViewPermissions(PermTestCase):

    def setUp(self):
        default_scenario_login()

    def test_test_view(self):
        url = reverse('example.test')
        self.assert_logged_in(url)

    def test_update_user_name(self):
        url = reverse(
            'update_user_name',
            kwargs=dict(pk=get_user_web().pk),
        )
        self.assert_staff_only(url)

    def test_update_user_password(self):
        url = reverse(
            'update_user_password',
            kwargs=dict(pk=get_user_web().pk),
        )
        self.assert_staff_only(url)
