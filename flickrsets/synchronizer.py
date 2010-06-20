"""
Flickr/database synchronizer of Django Flickrsets application.
"""
import logging
import time

from flickrsets import models
from flickrsets import settings as app_settings
from flickrsets.models import Photoset
from flickrsets.models import Photo
from flickrsets.models import RegisteredSet

log = logging.getLogger('flickrsets.synchronizer')


def run(client):
    """
    Runs the synchronization process.
    """
    flush_tables()
    photosets = RegisteredSet.objects.enabled()
    photosets_ids = [photoset.flickr_id for photoset in photosets]
    photo_kwargs = {
        'create_tags': app_settings.CREATE_TAGS,
        'save_exif_tags': app_settings.SAVE_EXIF_TAGS,
    }
    for photoset_id in photosets_ids:
        photoset, created = Photoset.objects.get_or_create_from_api(
            flickr_id=photoset_id,
            client=client,
            related_kwargs={'primary': photo_kwargs})
        photos_ids = Photoset.objects.get_photos_ids_from_api(
            flickr_id=photoset_id,
            client=client)
        for photo_id in photos_ids:
            photo, created = Photo.objects.get_or_create_from_api(
                flickr_id=photo_id,
                client=client,
                photoset=photoset,
                **photo_kwargs)
            time.sleep(app_settings.SYNCHRONIZER_PHOTO_TIME_SLEEP)
        time.sleep(app_settings.SYNCHRONIZER_PHOTOSET_TIME_SLEEP)


def flush_tables():
    """
    Flush tables.
    """
    model_names = ('Person', 'Photo', 'Photoset', 'Tag')
    for model_name in model_names:
        model = getattr(models, model_name)
        table = model._meta.db_table
        model.objects.all().delete()
        log.info(u'Flushed table: %s' % table)
