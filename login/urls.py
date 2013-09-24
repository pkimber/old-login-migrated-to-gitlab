from django.conf.urls import (
    patterns,
    url,
)
from django.core.urlresolvers import reverse_lazy
from django.views.generic.base import TemplateView

from registration.backends.default.views import ActivationView
from registration.backends.default.views import RegistrationView


urlpatterns = patterns(
    '',
    url(regex=r'^accounts/logout/$',
        view='django.contrib.auth.views.logout',
        kwargs={
            'next_page': reverse_lazy('project.home'),
            'template_name': 'login/logged_out.html',
        },
        name='logout'
        ),
)
