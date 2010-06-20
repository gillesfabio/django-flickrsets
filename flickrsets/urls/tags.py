"""
URLs of Django Flickrsets application related to ``Tag`` model.
"""
from django.conf.urls.defaults import patterns
from django.conf.urls.defaults import url


urlpatterns = patterns('flickrsets.views',
    url(r'^(?P<name>[-\w]+)/$',
        view='tag_photo_list',
        name='flickrsets-tag',
    ),
    url(r'^$',
        view='tag_list',
        name='flickrsets-tags',
    ),
)
