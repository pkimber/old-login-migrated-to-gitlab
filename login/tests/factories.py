# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

import factory

from django.contrib.auth.models import User


TEST_PASSWORD = 'letmein'


class UserFactory(factory.django.DjangoModelFactory):
    """Password is always set to 'pass'."""

    class Meta:
        model = User

    is_active = True
    is_staff = False
    is_superuser = False
    password = factory.PostGenerationMethodCall('set_password', TEST_PASSWORD)

    @factory.sequence
    def first_name(n):
        return 'first_name_{:02d}'.format(n)

    @factory.sequence
    def username(n):
        return 'user_{:02d}'.format(n)
