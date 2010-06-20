"""
Defaults URLs of Django Flickrsets application.
"""
from django.conf.urls.defaults import include
from django.conf.urls.defaults import patterns


urlpatterns = patterns('',
    (r'^people/', include('flickrsets.urls.people')),
    (r'^sets/', include('flickrsets.urls.photosets')),
    (r'^tags/', include('flickrsets.urls.tags')),
    (r'', include('flickrsets.urls.photos')),
)
