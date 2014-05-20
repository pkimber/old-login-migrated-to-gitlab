# -*- encoding: utf-8 -*-

from __future__ import unicode_literals
from django.contrib.auth.models import User

from login.tests.model_maker import (
    make_superuser,
    make_user,
)


STAFF = 'staff'


def get_user_fred():
    return User.objects.get(username='fred')


def get_user_mike():
    return User.objects.get(username='mike')


def get_user_sara():
    return User.objects.get(username='sara')


def get_user_staff():
    return User.objects.get(username=STAFF)


def get_user_web():
    return User.objects.get(username='web')


def default_scenario_login():
    """
    admin is a superuser
    staff is a member of staff
    web is a standard user with no extra permissions
    """
    super_user = make_superuser('admin')
    super_user.email = 'admin@pkimber.net'
    super_user.save()
    make_user(STAFF, email='staff@pkimber.net', is_staff=True)
    make_user(
        'web', email='web@pkimber.net',
        first_name='William', last_name='Webber'
    )


def user_contractor():
    """
    fred is a farmer
    mike is a merchant
    sara is a smallholder
    """
    make_user('fred', email='fred@pkimber.net')
    make_user('mike', email='mike@pkimber.net')
    make_user('sara', email='sara@pkimber.net')
