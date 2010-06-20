# -*- coding: utf-8
"""
Constants of Django Flickrsets application.
"""
from django.utils.translation import ugettext_lazy as _


# Prefix used for application's tables
APP_TABLE_PREFIX = 'flickrsets'

# Flickr's photo URLs
FLICKR_PHOTO_URL_SQUARE = 'sq'
FLICKR_PHOTO_URL_THUMBNAIL = 't'
FLICKR_PHOTO_URL_SMALL = 's'
FLICKR_PHOTO_URL_MEDIUM = 'm'
FLICKR_PHOTO_URL_LARGE = 'b'
FLICKR_PHOTO_URL_ORIGINAL = 'o'
FLICKR_PHOTO_URLS = (
    (FLICKR_PHOTO_URL_SQUARE, 'square', _('Square')),
    (FLICKR_PHOTO_URL_THUMBNAIL, 'thumbnail', _('Thumbnail')),
    (FLICKR_PHOTO_URL_SMALL, 'small', _('Small')),
    (FLICKR_PHOTO_URL_MEDIUM, 'medium', _('Medium')),
    (FLICKR_PHOTO_URL_LARGE, 'large', _('Large')),
    (FLICKR_PHOTO_URL_ORIGINAL, 'original', _('Original')))

# Flickr's photo URLs
FLICKR_PHOTO_SOURCE_SQUARE = 's'
FLICKR_PHOTO_SOURCE_THUMBNAIL = 't'
FLICKR_PHOTO_SOURCE_SMALL = 'm'
FLICKR_PHOTO_SOURCE_MEDIUM = 'default'
FLICKR_PHOTO_SOURCE_LARGE = 'b'
FLICKR_PHOTO_SOURCE_ORIGINAL = 'o'
FLICKR_PHOTO_SOURCES = (
    (FLICKR_PHOTO_SOURCE_SQUARE, 'square', _('Square')),
    (FLICKR_PHOTO_SOURCE_THUMBNAIL, 'thumbnail', _('Thumbnail')),
    (FLICKR_PHOTO_SOURCE_SMALL, 'small', _('Small')),
    (FLICKR_PHOTO_SOURCE_MEDIUM, 'medium', _('Medium')),
    (FLICKR_PHOTO_SOURCE_LARGE, 'large', _('Large')),
    (FLICKR_PHOTO_SOURCE_ORIGINAL, 'original', _('Original')))

# Flickr's genders
FLICKR_GENDER_FEMALE = 'F'
FLICKR_GENDER_MALE = 'M'
FLICKR_GENDER_OTHER = 'O'
FLICKR_GENDER_RATHER_NOT_SAY = 'X'
FLICKR_DEFAULT_GENDER = 'X'
FLICKR_GENDERS = (
    (FLICKR_GENDER_FEMALE, _('Female')),
    (FLICKR_GENDER_MALE, _('Male')),
    (FLICKR_GENDER_OTHER, _('Other')),
    (FLICKR_GENDER_RATHER_NOT_SAY, _('Rather not say')))

# Flickr's licenses
FLICKR_LICENSES = (
    (0, 'All Rights Reserved'),
    (1, 'Attribution-NonCommercial-ShareAlike License'),
    (2, 'Attribution-NonCommercial License'),
    (3, 'Attribution-NonCommercial-NoDerivs License'),
    (4, 'Attribution License'),
    (5, 'Attribution-ShareAlike License'),
    (6, 'Attribution-NoDerivs License'))

# Flickr's media
FLICKR_MEDIAS = (
    ('photo', _('Photo')),
    ('video', _('Video')),
    ('other', _('Other')))

# Test
TEST_PERSON_FLICKR_ID = u'94238521@N00'
TEST_PHOTO_FLICKR_ID = u'4242733600'
TEST_PHOTOSET_FLICKR_ID = u'72157623007721343'
TEST_TAG_RAW = u'rock'
