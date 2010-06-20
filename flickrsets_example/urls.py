# -*- coding: utf-8 -*-
# pylint: disable=W0611
import re

from django.conf import settings
from django.conf.urls.defaults import handler404
from django.conf.urls.defaults import handler500
from django.conf.urls.defaults import include
from django.conf.urls.defaults import patterns
from django.conf.urls.defaults import url
from django.contrib import admin

admin.autodiscover()


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('flickrsets.urls')),
)

urlpatterns += patterns('django.views.static',
    url(r'^%s(?P<path>.*)$' % re.escape(settings.MEDIA_URL.lstrip('/')),
        'serve',
        {'document_root': settings.MEDIA_ROOT},
    ),
)
