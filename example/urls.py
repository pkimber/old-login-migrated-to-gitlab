from django.conf.urls import (
    include, patterns, url,
)
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy
from django.views.generic import (
    RedirectView, TemplateView,
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
    url(regex=r'^accounts/',
        view=include('registration.backends.default.urls')
        ),
    url(regex=r'^$',
        view=TemplateView.as_view(template_name='example/home.html'),
        name='project.home'
        ),
    url(r'^home/user/$',
        view=RedirectView.as_view(url=reverse_lazy('project.home')),
        name='project.home.user'
        ),
    url(regex=r'^test/$',
        view=login_required(
            TemplateView.as_view(template_name='example/test.html'),
        ),
        name='example.test'
        ),
)
