# -*- encoding: utf-8 -*-
from django import forms
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User

from base.form_utils import RequiredFieldForm

from .models import username_validator


class PasswordResetNotifyForm(PasswordResetForm):

    pass



class UserCreationForm(RequiredFieldForm):
    """Copied from Django, 'UserCreationForm'.

    Designed to be used with a model derived from 'AbstractBaseUser'.
    'Meta', 'fields' should include 'password1' and 'password2'.

    """

    password1 = forms.CharField(
        label="Password", widget=forms.PasswordInput
    )
    password2 = forms.CharField(
        label="Confirm Password", widget=forms.PasswordInput,
        help_text="Enter the same password as above, for verification."
    )

    def clean_username(self):
        """Clean the user name - check it doesn't already exist.

        Derived classes should call this method to get the 'username' before
        adding their own validation.

        """
        username = self.cleaned_data["username"]
        try:
            User._default_manager.get(username=username)
            raise forms.ValidationError(
                "A user with that username already exists."
            )
        except User.DoesNotExist:
            pass
        return username

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                "The two password fields didn't match."
            )
        return password2


class UserNameForm(RequiredFieldForm):
    """A member of staff can change the user name of a user."""

    username = forms.RegexField(
        label='Username',
        max_length=30,
        regex=r"^[\w.@+-]+$",
        help_text=(
            '30 characters or fewer. Letters, numbers, '
            'dot, dash and underscore.'
        ),
        error_messages={
            'invalid': (
                "This value may contain only letters, numbers and "
                "dot, dash and underscore."
            )
        }
    )

    class Meta:
        model = User
        fields = ('username',)


class UserUsernameCreationForm(UserCreationForm):

    username = forms.CharField(
        max_length=30,
        help_text=(
            '30 characters or fewer. Letters, numbers, '
            'dot, dash and underscore.'
        ),
        validators=[username_validator]
    )
