# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.contrib.auth import (
    authenticate,
    login,
)
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.views.generic import CreateView


class RegisterCreateView(CreateView):

    form_class = UserCreationForm
    model = User
    template_name = 'login/register.html'

    def form_valid(self, form):
        username = form.clean_username()
        password = form.clean_password2()
        self.object = form.save()
        # log in the user
        user = authenticate(username=username, password=password)
        if user:
            login(self.request, user)
        return super(RegisterCreateView, self).form_valid(form)

    def get_success_url(self):
        return settings.LOGIN_REDIRECT_URL
