"""
Settings of Django Flickrsets application.
"""
from django.conf import settings


# Flickr
# -----------------------------------------------------------------------------
FLICKR_API_KEY = getattr(
    settings,
    'FLICKRSETS_FLICKR_API_KEY',
    None)

FLICKR_USER_ID = getattr(
    settings,
    'FLICKRSETS_FLICKR_USER_ID',
    None)

# Tags
# -----------------------------------------------------------------------------
CREATE_TAGS = getattr(
    settings,
    'FLICKRSETS_CREATE_TAGS',
    True)

# EXIF Tags
# -----------------------------------------------------------------------------
SAVE_EXIF_TAGS = getattr(
    settings,
    'FLICKRSETS_SAVE_EXIF_TAGS',
    True)

EXIF_TAG_SPACE_LIST = getattr(
    settings,
    'FLICKRSETS_EXIF_TAG_SPACE_LIST',
    ('ExifIFD', 'IPTC'))

# Views
# -----------------------------------------------------------------------------
PERSON_LIST_VIEW_PAGINATE_BY = getattr(
    settings,
    'FLICKRSETS_PERSON_LIST_VIEW_PAGINATE_BY',
    10)
    
PERSON_PHOTO_LIST_VIEW_PAGINATE_BY = getattr(
    settings,
    'FLICKRSETS_PERSON_PHOTO_LIST_VIEW_PAGINATE_BY',
    10)

PHOTO_LIST_VIEW_PAGINATE_BY = getattr(
    settings,
    'FLICKRSETS_PHOTO_LIST_VIEW_PAGINATE_BY',
    10)

PHOTOSET_LIST_VIEW_PAGINATE_BY = getattr(
    settings,
    'FLICKRSETS_PHOTOSET_LIST_VIEW_PAGINATE_BY',
    10)

PHOTOSET_PHOTO_LIST_VIEW_PAGINATE_BY = getattr(
    settings,
    'FLICKRSETS_PHOTOSET_PHOTO_LIST_VIEW_PAGINATE_BY',
    10)
    
TAG_PHOTO_LIST_VIEW_PAGINATE_BY = getattr(
    settings,
    'FLICKRSETS_TAG_PHOTO_LIST_VIEW_PAGINATE_BY',
    10)

# Synchronizer
# -----------------------------------------------------------------------------
SYNCHRONIZER_PHOTO_TIME_SLEEP = getattr(
    settings,
    'FLICKRSETS_SYNCHRONIZER_PHOTO_TIME_SLEEP',
    1)

SYNCHRONIZER_PHOTOSET_TIME_SLEEP = getattr(
    settings,
    'FLICKRSETS_SYNCHRONIZER_PHOTOSET_TIME_SLEEP',
    1)
