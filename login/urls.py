from django.conf.urls import (
    patterns,
    url,
)
from django.core.urlresolvers import reverse_lazy

from .views import RegisterCreateView


urlpatterns = patterns(
    '',
    url(regex=r'^accounts/login/$',
        view='django.contrib.auth.views.login',
        kwargs={
            'template_name': 'login/login.html',
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
    url(regex=r'^accounts/register/$',
        view=RegisterCreateView.as_view(),
        name='register'
        ),
)
