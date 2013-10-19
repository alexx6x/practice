from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'practice_3.views.home', name='home'),
    # url(r'^practice_3/', include('practice_3.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

    url(r'^$', 'url.views.listing', name='listing'),
    url(r'^log/(?P<temp>([-,.\w]*/)*)$','url.views.listing', name='listing'),
)