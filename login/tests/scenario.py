from django.contrib.auth.models import User

from login.tests.model_maker import (
    make_superuser,
    make_user,
)


STAFF = 'staff'


def get_user_fred():
    return User.objects.get(username='fred')


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
    make_superuser('admin')
    make_user(STAFF, is_staff=True)
    make_user('web')


def user_contractor():
    """
    fred is a farmer
    sara is a smallholder
    """
    make_user('fred')
    make_user('sara')
