from django.contrib.auth.models import User
from django.utils import timezone


def make_user(user_name, password=None, **kwargs):
    """ Some code copied from 'contrib.auth.models.create_user' """
    if not password:
        password = user_name
    defaults = {
        'date_joined': timezone.now(),
        'is_active': True,
        'is_staff': False,
        'is_superuser': False,
    }
    defaults.update(kwargs)
    user = User(
        username=user_name,
        **defaults
    )
    user.set_password(password)
    user.save()
    return user


def make_superuser(user_name, password=None):
    if not password:
        password = user_name
    return User.objects.create_superuser(user_name, '', password)
