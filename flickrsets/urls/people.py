"""
URLs of Django Flickrsets application related to ``Person`` model.
"""
from django.conf.urls.defaults import patterns
from django.conf.urls.defaults import url


urlpatterns = patterns('flickrsets.views',
    url(r'^(?P<flickr_id>[-@\w]+)/$',
        view='person_photo_list',
        name='flickrsets-person',
    ),
    url(r'^$',
        view='person_list',
        name='flickrsets-people',
    ),
)
