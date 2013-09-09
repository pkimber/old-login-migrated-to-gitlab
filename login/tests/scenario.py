from django.contrib.auth.models import User

from login.tests.model_maker import (
    make_superuser,
    make_user,
)


def get_user_fred():
    return User.objects.get(username='fred')


def get_user_sara():
    return User.objects.get(username='sara')


def get_user_staff():
    return User.objects.get(username='staff')


def user_default():
    # superuser
    make_superuser('admin')
    # member of staff
    make_user('staff', is_staff=True)
    # standard user with no extra permissions
    make_user('web')


def user_contractor():
    # fred is a farmer
    make_user('fred')
    # steph is a smallholder
    make_user('sara')
