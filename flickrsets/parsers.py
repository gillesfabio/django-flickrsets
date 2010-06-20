"""
Flickr parser classes of Django Flickrsets application.
"""
import logging

from django.utils.encoding import smart_unicode

from flickrsets import models
from flickrsets import settings as app_settings

log = logging.getLogger('flickrsets.parsers')


# Base classes
# -----------------------------------------------------------------------------
class BaseParser(object):
    """
    Parser base class.
    """
    model = None
    fields_map = None
    fk_fields_map = None

    def __init__(self, flickr_id=None, client=None):
        """
        Parser initialization.
        """
        self.flickr_id = flickr_id
        self.client = client

    def raw_data(self):
        """
        Returns data to format returned by Flickr API.
        """
        pass
        
    def formatted_data(self):
        """
        Returns data of ``raw_data()`` formatted for object creation.
        """
        return self.format_raw_data()

    def format_raw_data(self):
        """
        Formats data of ``raw_data()`` for object creation.
        """
        raw_data = self.raw_data()
        is_list = True
        if not isinstance(raw_data, list):
            is_list = False
            raw_data = [raw_data]
        items = []
        for item in raw_data:
            formatted_data = {}
            if self.fields_map:
                formatted_data['kwargs'] = self.format_data_for_fields(
                    self.fields_map,
                    item)
            if self.fk_fields_map:
                formatted_data['fk_fields'] = self.format_data_for_fk_fields(
                    self.fk_fields_map,
                    item)
            items.append(formatted_data)
        if not is_list:
            items = items[0]
        return items

    def format_data_for_fields(self, fields_map, raw_data, model=None):
        """
        Formats data of ``fields_map`` fields.
        """
        formatted_data = {}
        if model is None:
            model = self.model
        for field_name, api_name in fields_map:
            field = model._meta.get_field_by_name(field_name)[0]
            value = self.get_raw_value(api_name, raw_data)
            field_value = self.get_safe_value_for_field(field, value)
            if field_value is not None:
                formatted_data[field_name] = field_value
        return formatted_data

    def format_data_for_fk_fields(self, fields_map, raw_data):
        """
        Formats data of ``fk_fields_map`` fields.
        """
        formatted_data = {}
        for field_name, api_name in fields_map:
            value = self.get_raw_value(api_name, raw_data)
            field_value = self.get_safe_value(value, 'str')
            formatted_data[field_name] = field_value
        return formatted_data

    def get_raw_value(self, key, dictionary):
        """
        Returns the raw value of the given ``key`` in the given ``dictionary``.
        """
        if dictionary is not None:
            keys = key.split('.')
            if len(keys) == 2:
                return dictionary.get(keys[0]).get(keys[1])
            return dictionary.get(key)

    def get_safe_value_for_field(self, field, value):
        """
        Returns safe value for ``value`` for a given ``field``.
        """
        from django.db.models import fields
        is_int = isinstance(field, fields.IntegerField)
        is_char = isinstance(field, fields.CharField)
        is_text = isinstance(field, fields.TextField)
        is_date = isinstance(field, fields.DateField)
        is_datetime = isinstance(field, fields.DateTimeField)
        if is_char or is_text:
            return self.get_safe_value(value, 'str')
        if is_int:
            return self.get_safe_value(value, 'int')
        if is_date or is_datetime:
            return self.get_safe_value(value, 'date')

    def get_safe_value(self, value, kind='str'):
        """
        Returns safe value for ``value`` for a given ``kind``.
        """
        from flickrsets import utils
        if value is not None:
            if isinstance(value, dict):
                return value.get('_content', None)
            if kind == 'str':
                return smart_unicode(value)
            if kind == 'int':
                return utils.safe_int(value)
            if kind == 'date':
                return utils.parse_date(value)


# Models parsers
# -----------------------------------------------------------------------------
class PersonParser(BaseParser):
    """
    Parser mapped on ``Person`` model which returns data for a given person
    Flickr ID.
    """
    model = models.Person
    
    fields_map = (
        ('flickr_id', 'nsid'),
        ('username', 'username'),
        ('realname', 'realname'),
        ('photos_url', 'photosurl'),
        ('profile_url', 'profileurl'),
        ('mobile_url', 'mobileurl'),
        ('icon_server', 'iconserver'),
        ('icon_farm', 'iconfarm'),
        ('gender', 'gender'),
        ('location', 'location'),
        ('photos_count', 'photos.count'))
    
    def raw_data(self):
        """
        Returns data returned by ``flickr.people.getInfo``.
        """
        log.info(u'PersonParser -- flickr.people.getInfo()')
        json = self.client.people.getInfo(user_id=self.flickr_id)
        return json.get('person')


class PhotoParser(BaseParser):
    """
    Parser mapped on ``Photo`` model which returns data for a given photo
    Flickr ID.
    """
    model = models.Photo
    
    fields_map = (
        ('flickr_id', 'id'),
        ('title', 'title'),
        ('description', 'description'),
        ('server', 'server'),
        ('farm', 'farm'),
        ('license', 'license'),
        ('media', 'media'),
        ('secret', 'secret'),
        ('original_secret', 'originalsecret'),
        ('original_format', 'originalformat'),
        ('views_count', 'views'),
        ('comments_count', 'comments'),
        ('date_uploaded', 'dateuploaded'),
        ('date_posted', 'dates.posted'),
        ('date_updated', 'dates.lastupdate'),
        ('date_taken', 'dates.taken'))
        
    fk_fields_map = (
        ('owner', 'owner.nsid'),)

    def raw_data(self):
        """
        Returns data returned by ``flickr.photos.getInfo``.
        """
        log.info(u'PhotoParser -- flickr.photos.getInfo()')
        json = self.client.photos.getInfo(photo_id=self.flickr_id)
        return json.get('photo')

    def get_exif(self):
        """
        Returns data returned by ``flickr.photos.getExif``.
        """
        log.info(u'PhotoExifTagsParser -- flickr.photos.getExif()')
        json = self.client.photos.getExif(photo_id=self.flickr_id)
        tags = json['photo']['exif']
        spaces = app_settings.EXIF_TAG_SPACE_LIST
        tags = [tag for tag in tags if tag['tagspace'] in spaces]
        return self._convert_exif(tags)
        
    def _convert_exif(self, exif):
        """
        Converts EXIF data.
        """
        converted = {}
        for e in exif:
            key = smart_unicode(e['label'])
            val = e.get('clean', e['raw'])['_content']
            val = smart_unicode(val)
            converted[key] = val
        return converted


class PhotosetParser(BaseParser):
    """
    Parser mapped on ``Photoset`` model which returns data for a given photoset
    Flickr ID.
    """
    model = models.Photoset
    
    fields_map = (
        ('flickr_id', 'id'),
        ('title', 'title'),
        ('description', 'description'),
        ('server', 'server'),
        ('farm', 'farm'),
        ('photos_count', 'photos'))
        
    fk_fields_map = (
        ('owner', 'owner'),
        ('primary', 'primary'))

    def raw_data(self):
        """
        Returns data returned by ``flickr.photosets.getInfo``.
        """
        log.info(u'PhotosetParser -- flickr.photosets.getInfo()')
        json = self.client.photosets.getInfo(
            photoset_id=self.flickr_id)
        return json.get('photoset')

    def get_photos_ids(self):
        """
        Returns a list of photos IDs of the photoset.
        Calls ``flickr.photosets.getPhotos``.
        """
        log.info(u'PhotosetParser -- flickr.photosets.getPhotos()')
        json = self.client.photosets.getPhotos(
            photoset_id=self.flickr_id)
        photos = json.get('photoset').get('photo')
        return [self.get_safe_value(p.get('id'), 'str') for p in photos]


class PhotoTagsParser(BaseParser):
    """
    Parser mapped on ``Tag`` model which returns data for related ``Tag``
    objects of a given photo Flickr ID.
    """
    model = models.Tag
    
    fields_map = (
        ('flickr_id', 'id'),
        ('name', '_content'),
        ('raw', 'raw'))
        
    fk_fields_map = (
        ('author', 'author'),)

    def raw_data(self):
        """
        Returns data returned by ``flickr.tags.getListPhoto``.
        """
        log.info(u'PhotoTagParser -- flickr.tags.getListPhoto')
        json = self.client.tags.getListPhoto(photo_id=self.flickr_id)
        return json.get('photo').get('tags').get('tag')
