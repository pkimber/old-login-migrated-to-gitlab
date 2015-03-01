# -*- encoding: utf-8 -*-
from django.core import mail
from django.core.urlresolvers import reverse
from django.test import TestCase

from login.tests.factories import UserFactory


class TestPasswordReset(TestCase):

    def test_password_reset_email(self):
        UserFactory(username='web', email='test@pkimber.net')
        response = self.client.post(
            reverse('password_reset'),
            data=dict(email='test@pkimber.net'),
        )
        self.assertRedirects(response, reverse('password_reset_done'))
        # Test that one message has been sent.
        assert 1 == len(mail.outbox)
        assert 'Password reset on testserver' == mail.outbox[0].subject

    def test_password_reset_email_does_not_exist(self):
        response = self.client.post(
            reverse('password_reset'),
            data=dict(email='test@pkimber.net'),
        )
        self.assertRedirects(response, reverse('password_reset_done'))
        # Check that no emails have been sent.
        assert not len(mail.outbox)
