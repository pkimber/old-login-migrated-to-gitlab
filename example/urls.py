# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import (
    include,
    patterns,
    url,
)
from django.contrib import admin
from django.core.urlresolvers import reverse_lazy
from django.views.generic import (
    RedirectView,
    TemplateView,
)

from login.views import RegisterCreateView

from .views import (
    MyUpdateUserNameView,
    MyUpdateUserPasswordView,
    TestView,
)


admin.autodiscover()


urlpatterns = patterns(
    '',
    url(regex=r'^admin/',
        view=include(admin.site.urls)
        ),
    url(regex=r'^',
        view=include('login.urls')
        ),
    url(regex=r'^$',
        view=TemplateView.as_view(template_name='example/home.html'),
        name='project.home'
        ),
    url(r'^home/user/$',
        view=RedirectView.as_view(url=reverse_lazy('example.test')),
        name='project.dash'
        ),
    url(regex=r'^test/$',
        view=TestView.as_view(),
        name='example.test'
        ),
    url(regex=r'^accounts/register/$',
        view=RegisterCreateView.as_view(),
        name='register'
        ),
    url(regex=r'^accounts/user/(?P<pk>\d+)/username/$',
        view=MyUpdateUserNameView.as_view(),
        name='update_user_name',
        ),
    url(regex=r'^accounts/user/(?P<pk>\d+)/password/$',
        view=MyUpdateUserPasswordView.as_view(),
        name='update_user_password',
        ),
)
