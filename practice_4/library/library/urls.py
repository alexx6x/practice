from django.conf.urls import url, patterns


urlpatterns = patterns(
    'bks.bks',
    url(r'^lib/$', 'gets'),
    url(r'^lib/(?P<bookId>\d+)/?$', 'get'),
)


urlpatterns += patterns(
    'bks.au',
    url(r'^lib/authors/$', 'gets'),
    url(r'^lib/authors/(?P<authorId>\d+)/?$', 'get'),
)