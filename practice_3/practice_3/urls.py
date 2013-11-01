from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'url.views.listing', name='listing'),
    url(r'^log/(?P<temp>([-,.\w]*/)*)$', 'url.views.listing', name='listing'),
)
