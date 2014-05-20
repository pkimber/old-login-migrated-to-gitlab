# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import (
    patterns,
    url,
)
from django.contrib.auth.views import (
    password_reset,
    password_reset_done,
)
from django.core.urlresolvers import reverse_lazy


urlpatterns = patterns(
    '',
    url(regex=r'^accounts/login/$',
        view='django.contrib.auth.views.login',
        kwargs={
            'template_name': 'project/login.html',
        },
        name='login'
        ),
    url(regex=r'^accounts/logout/$',
        view='django.contrib.auth.views.logout',
        kwargs={
            'next_page': reverse_lazy('project.home'),
            'template_name': 'login/logged_out.html',
        },
        name='logout'
        ),
    url(regex=r'^accounts/password/change/$',
        view='django.contrib.auth.views.password_change',
        kwargs={
            'template_name': 'project/password_change.html',
        },
        name='password_change'
        ),
    url(regex=r'^accounts/password/change/done/$',
        view='django.contrib.auth.views.password_change_done',
        kwargs={
            'template_name': 'project/password_change_done.html',
        },
        name='password_change_done'
        ),
    url(regex=r'^accounts/password/reset/$',
        view=password_reset,
        kwargs={
            'template_name': 'project/password_reset.html'
        },
        name='password_reset'
        ),
    url(regex=r'^accounts/password/reset/done/$',
        view=password_reset_done,
        kwargs={
            'template_name': 'project/password_reset_done.html'
        },
        name='password_reset_done'
        ),
)
