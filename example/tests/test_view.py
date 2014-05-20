# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.test import TestCase


from login.tests.scenario import (
    default_scenario_login,
    get_user_staff,
    get_user_web,
)

class TestUpdateUserPassword(TestCase):

    def setUp(self):
        default_scenario_login()
        staff = get_user_staff()
        self.client.login(
            username=staff.username, password=staff.username
        )

    def test_update_user_name(self):
        user = get_user_web()
        url = reverse(
            'update_user_name',
            kwargs=dict(pk=user.pk),
        )
        self.assertEqual('web', user.username)
        self.client.post(
            url,
            dict(
                username='webber',
            )
        )
        user = User.objects.get(username='webber')
        self.assertEqual('webber', user.username)

    def test_update_user_password(self):
        user = get_user_web()
        url = reverse(
            'update_user_password',
            kwargs=dict(pk=user.pk),
        )
        response = self.client.post(
            url,
            dict(
                new_password1='123',
                new_password2='123',
            )
        )
        self.assertEqual(response.status_code, 302)
