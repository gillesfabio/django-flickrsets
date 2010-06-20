"""
URLs of Django Flickrsets application related to ``Photo`` model.
"""
from django.conf.urls.defaults import patterns
from django.conf.urls.defaults import url


urlpatterns = patterns('flickrsets.views',
    url(r'^(?P<flickr_id>[-\w]+)/$',
        view='photo_detail',
        name='flickrsets-photo',
    ),
    url(r'^$',
        view='photo_list',
        name='flickrsets-photos',
    ),
)
