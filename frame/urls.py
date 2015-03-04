from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings


from frame.views import *

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'frame.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^about/$', about),
    url(r'^contact/$', contact),
    url(r'^thanks/$', thanks),
    url(r'^sent/$', contact),
    url(r'^gallery/$', gallery),
    url(r'^projects/$', projects),
    url(r'^projects/([A-Za-z0-9]{3,20})/$', project),
    #url(r'^gallery/[A-Za-z0-9]{3,20}/([0-9]{1,3}.png)$', image),

)

urlpatterns += staticfiles_urlpatterns()


if settings.DEBUG:
# Serve static files in debug.
    urlpatterns += patterns('',
        (r'^projects/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT,
        'show_indexes' : True}),
    )