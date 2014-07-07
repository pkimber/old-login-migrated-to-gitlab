# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

import factory

from django.contrib.auth.models import User


class UserFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = User

    username = factory.Sequence(lambda n: 'user_{:02d}'.format(n))
