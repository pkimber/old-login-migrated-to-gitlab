from django.conf.urls import (
    patterns,
    url,
)
from django.core.urlresolvers import reverse_lazy


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
