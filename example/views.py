# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from base.view_utils import BaseMixin

from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.views.generic import TemplateView

from braces.views import LoginRequiredMixin

from login.views import (
    UpdateUserNameView,
    UpdateUserPasswordView,
)


class MyUpdateUserNameView(UpdateUserNameView):

    def get_success_url(self):
        return reverse('example.test')


class MyUpdateUserPasswordView(UpdateUserPasswordView):

    def get_success_url(self):
        return reverse('example.test')


class TestView(LoginRequiredMixin, BaseMixin, TemplateView):

    template_name = 'example/test.html'

    def get_context_data(self, **kwargs):
        context = super(TestView, self).get_context_data(**kwargs)
        if self.request.user.is_staff:
            context.update(dict(
                request_user=self.request.user,
                users=User.objects.all(),
            ))
        return context
