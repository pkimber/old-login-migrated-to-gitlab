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
    # urls.py copied from registration app:
    # ('registration/backends/default/urls.py')
    url(regex=r'^activate/complete/$',
        view=TemplateView.as_view(
            template_name='registration/activation_complete.html'
        ),
        name='registration_activation_complete'),
    # Activation keys get matched by \w+ instead of the more specific
    # [a-fA-F0-9]{40} because a bad activation key should still get to the
    # view; that way it can return a sensible "invalid key" message instead
    # of a confusing 404.
    url(regex=r'^activate/(?P<activation_key>\w+)/$',
        view=ActivationView.as_view(),
        name='registration_activate'),
    url(regex=r'^register/$',
        view=RegistrationView.as_view(),
        name='registration_register'),
    url(regex=r'^register/complete/$',
        view=TemplateView.as_view(
            template_name='registration/registration_complete.html'
        ),
        name='registration_complete'),
    url(regex=r'^register/closed/$',
        view=TemplateView.as_view(
            template_name='registration/registration_closed.html'
        ),
        name='registration_disallowed'),
)
