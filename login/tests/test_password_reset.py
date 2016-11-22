# -*- encoding: utf-8 -*-
import pytest

from django.core import mail
from django.core.urlresolvers import reverse

from login.tests.factories import UserFactory
from mail.models import Mail
from mail.tests.factories import NotifyFactory


@pytest.mark.django_db
def test_password_reset_email(client, mailoutbox):
    """Send a notification email and a reset email."""
    NotifyFactory()
    UserFactory(username='web', email='test@pkimber.net')
    response = client.post(
        reverse('password_reset'),
        data=dict(email='test@pkimber.net'),
    )
    assert 302 == response.status_code
    assert reverse('password_reset_done') in response['Location']
    result = [outbox.subject for outbox in mail.outbox]
    assert 1 == len(mailoutbox)
    assert 'Password reset on testserver' in result
    assert 1 == Mail.objects.count()
    obj = Mail.objects.first()
    assert obj.message.subject == 'Password reset request from test@pkimber.net'


@pytest.mark.django_db
def test_password_reset_email_does_not_exist(client, mailoutbox):
    """Only send a notification if email address doesn't exist."""
    NotifyFactory()
    response = client.post(
        reverse('password_reset'),
        data=dict(email='test@pkimber.net'),
    )
    assert 302 == response.status_code
    assert reverse('password_reset_done') in response['Location']
    # Check that only the request notification email has been sent.
    assert 0 == len(mailoutbox)
    assert 1 == Mail.objects.count()
    obj = Mail.objects.first()
    assert obj.message.subject == 'Password reset request from test@pkimber.net'
