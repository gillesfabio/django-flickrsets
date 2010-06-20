"""
URLs of Django Flickrsets application related to ``Photoset`` model.
"""
from django.conf.urls.defaults import patterns
from django.conf.urls.defaults import url


urlpatterns = patterns('flickrsets.views',
    url(r'^(?P<flickr_id>[-\w]+)/$',
        view='photoset_photo_list',
        name='flickrsets-photoset',
    ),
    url(r'^$',
        view='photoset_list',
        name='flickrsets-photosets',
    ),
)
