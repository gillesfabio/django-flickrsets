"""
Models of Django Flickrsets application.
"""
from django.db import models
from django.utils import simplejson
from django.utils.translation import ugettext_lazy as _

from flickrsets import constants
from flickrsets.managers import PersonManager
from flickrsets.managers import PhotoManager
from flickrsets.managers import PhotosetManager
from flickrsets.managers import RegisteredSetManager
from flickrsets.managers import TagManager


class RegisteredSet(models.Model):
    """
    A registered Flickr Set.
    """
    flickr_id = models.CharField(
        verbose_name=_('Flickr ID'),
        max_length=255,
        unique=True)

    title = models.CharField(
        verbose_name=_('title'),
        max_length=255)

    enabled = models.BooleanField(
        verbose_name=_('enabled'),
        default=True)

    objects = RegisteredSetManager()

    class Meta:
        """
        Model metadata.
        """
        db_table = '%s_registered_set' % constants.APP_TABLE_PREFIX
        verbose_name = _('registered set')
        verbose_name_plural = _('registered sets')

    def __unicode__(self):
        """
        Object's human readable unicode string.
        """
        return u'%s - %s' % (self.title, self.flickr_id)


class Person(models.Model):
    """
    A Flickr Person (User).
    """
    flickr_id = models.CharField(
        verbose_name=_('flickr ID'),
        max_length=255)

    username = models.CharField(
        verbose_name=_('username'),
        max_length=255,
        null=True,
        blank=True)

    realname = models.CharField(
        verbose_name=_('realname'),
        max_length=255,
        null=True,
        blank=True)

    photos_url = models.CharField(
        verbose_name=_('photos URL'),
        max_length=255)

    profile_url = models.CharField(
        verbose_name=_('profile URL'),
        max_length=255)

    mobile_url = models.CharField(
        verbose_name=_('mobile URL'),
        max_length=255)

    icon_server = models.IntegerField(
        verbose_name=_('icon server'),
        null=True,
        blank=True)

    icon_farm = models.IntegerField(
        verbose_name=_('icon farm'),
        null=True,
        blank=True)

    gender = models.CharField(
        verbose_name=_('gender'),
        max_length=1,
        choices=constants.FLICKR_GENDERS,
        default=constants.FLICKR_DEFAULT_GENDER,
        blank=True)

    location = models.CharField(
        verbose_name=_('location'),
        max_length=255,
        null=True,
        blank=True)

    photos_count = models.IntegerField(
        verbose_name=_('photos count'),
        null=True,
        blank=True)

    objects = PersonManager()

    class Meta:
        """
        Model metadata.
        """
        db_table = '%s_person' % constants.APP_TABLE_PREFIX
        ordering = ('flickr_id',)
        verbose_name = _('person')
        verbose_name_plural = _('persons')

    def __unicode__(self):
        """
        Object's human readable unicode string.
        """
        return u'%s' % self.name

    @models.permalink
    def get_absolute_url(self):
        """
        Returns object's absolute URL.
        """
        return ('flickrsets-person', (), {'flickr_id': self.flickr_id})

    @property
    def name(self):
        """
        Returns person name.
        """
        return self.realname or self.username or self.flickr_id

    @property
    def buddy_icon_url(self):
        """
        Returns person's buddy icon URL.
        """
        if self.icon_farm and self.icon_server:
            return u'http://farm%s.static.flickr.com/%s/buddyicons/%s.jpg' % (
                self.icon_farm,
                self.icon_server,
                self.flickr_id)
        return u'http://www.flickr.com/images/buddyicon.jpg'


class Photoset(models.Model):
    """
    A Flickr Photoset.
    """
    owner = models.ForeignKey(
        'flickrsets.Person',
        verbose_name=_('owner'),
        related_name='photosets')

    primary = models.ForeignKey(
        'flickrsets.Photo',
        verbose_name=_('primary'),
        related_name='photoset_primaries')

    flickr_id = models.CharField(
        verbose_name=_('flickr ID'),
        max_length=255)

    title = models.CharField(
        verbose_name=_('title'),
        max_length=255)

    description = models.TextField(
        verbose_name=_('description'),
        null=True,
        blank=True)

    server = models.IntegerField(
        verbose_name=_('server'),
        null=True,
        blank=True)

    farm = models.IntegerField(
        verbose_name=_('farm'),
        null=True,
        blank=True)

    photos_count = models.IntegerField(
        verbose_name=_('photos'),
        null=True,
        blank=True)

    objects = PhotosetManager()

    class Meta:
        """
        Model metadata.
        """
        db_table = '%s_photoset' % constants.APP_TABLE_PREFIX
        ordering = ('title',)
        verbose_name = _('photoset')
        verbose_name_plural = _('photosets')

    def __unicode__(self):
        """
        Object's human readable unicode string.
        """
        return u'%s' % self.title

    @models.permalink
    def get_absolute_url(self):
        """
        Returns object's absolute URL.
        """
        return ('flickrsets-photoset', (), {'flickr_id': self.flickr_id})

    def get_flickr_url(self):
        """
        Returns object's Flickr URL.
        """
        return u'http://flickr.com/photos/%s/sets/%s/' % (
            self.owner.photos_url,
            self.flickr_id)


class Photo(models.Model):
    """
    A Flickr Photo.
    """
    photoset = models.ForeignKey(
        'flickrsets.Photoset',
        verbose_name=_('photoset'),
        related_name='photos',
        null=True,
        blank=True)

    owner = models.ForeignKey(
        'flickrsets.Person',
        verbose_name=_('owner'),
        related_name='photos')

    tags = models.ManyToManyField(
        'flickrsets.Tag',
        verbose_name=_('tags'),
        null=True,
        blank=True,
        related_name='photos')

    flickr_id = models.CharField(
        verbose_name=_('flickr ID'),
        max_length=255)

    title = models.CharField(
        verbose_name=_('title'),
        max_length=255)

    description = models.TextField(
        verbose_name=_('description'),
        null=True,
        blank=True)

    server = models.IntegerField(
        verbose_name=_('server'))

    farm = models.IntegerField(
        verbose_name=_('farm'))

    license = models.SmallIntegerField(
        verbose_name=_('license'),
        choices=constants.FLICKR_LICENSES,
        null=True,
        blank=True)

    media = models.CharField(
        verbose_name=_('media'),
        max_length=10,
        choices=constants.FLICKR_MEDIAS,
        null=True,
        blank=True)

    secret = models.CharField(
        verbose_name=_('secret'),
        max_length=255)

    original_secret = models.CharField(
        verbose_name=_('original secret'),
        max_length=255,
        null=True,
        blank=True)

    original_format = models.CharField(
        verbose_name=_('original format'),
        max_length=10,
        null=True,
        blank=True)

    views_count = models.IntegerField(
        verbose_name=_('views'),
        null=True,
        blank=True)

    comments_count = models.IntegerField(
        verbose_name=_('comments'),
        null=True,
        blank=True)

    date_uploaded = models.DateTimeField(
        verbose_name=_('date uploaded'),
        null=True,
        blank=True)

    date_posted = models.DateTimeField(
        verbose_name=_('date posted'),
        null=True,
        blank=True)

    date_updated = models.DateTimeField(
        verbose_name=_('date updated'),
        null=True,
        blank=True)

    date_taken = models.DateTimeField(
        verbose_name=_('date taken'),
        null=True,
        blank=True)
        
    _exif = models.TextField(
        verbose_name=_('EXIF'),
        null=True,
        blank=True)

    objects = PhotoManager()

    class Meta:
        """
        Model metadata.
        """
        db_table = '%s_photo' % constants.APP_TABLE_PREFIX
        ordering = ('title',)
        verbose_name = _('photo')
        verbose_name_plural = _('photos')

    def __unicode__(self):
        """
        Object's human readable string.
        """
        return u'%s' % self.title

    def __getattr__(self, name):
        """
        Overrides ``__getattr__`` to adds dynamic properties.
        """
        # image_VERSION_url properties
        for size, size_rname, size_name in constants.FLICKR_PHOTO_URLS:
            if name in ('image_url', 'image_medium_url'):
                medium_size = constants.FLICKR_PHOTO_URL_MEDIUM
                return self.get_image_url(size=medium_size)
            if name == 'image_%s_url' % size_rname:
                return self.get_image_url(size=size)
        # image_VERSION_source properties
        for size, size_rname, size_name in constants.FLICKR_PHOTO_SOURCES:
            if name in ('image_source', 'image_medium_source'):
                medium_size = constants.FLICKR_PHOTO_SOURCE_MEDIUM
                return self.get_image_source(size=medium_size)
            if name == 'image_%s_source' % size_rname:
                return self.get_image_source(size=size)
        models.Model.__getattribute__(self, name)

    @models.permalink
    def get_absolute_url(self):
        """
        Returns object's absolute URL.
        """
        return ('flickrsets-photo', (), {'flickr_id': self.flickr_id})
    
    def _set_exif(self, d):
        """
        ``_exif`` field setter.
        """
        self._exif = simplejson.dumps(d)
        
    def _get_exif(self):
        """
        ``_exif`` field getter.
        """
        if self._exif:
            return simplejson.loads(self._exif)
        else:
            return {}
    
    exif = property(_get_exif, _set_exif, "Photo EXIF data, as a dictionary.")
    
    def get_image_source(self, size=None):
        """
        Returns object's image source.
        """
        sources = constants.FLICKR_PHOTO_SOURCES
        sizes = [abbrev for abbrev, rname, name in sources]
        if size in sizes and size != constants.FLICKR_PHOTO_SOURCE_MEDIUM:
            secret = self.secret
            if size == constants.FLICKR_PHOTO_SOURCE_ORIGINAL:
                secret = self.original_secret
            return u'http://farm%s.static.flickr.com/%s/%s_%s_%s.jpg' % (
                self.farm,
                self.server,
                self.flickr_id,
                secret,
                size)
        else:
            return u'http://farm%s.static.flickr.com/%s/%s_%s.jpg' % (
                self.farm,
                self.server,
                self.flickr_id,
                self.secret)

    def get_image_url(self, size=None):
        """
        Returns object's image URL.
        """
        urls = constants.FLICKR_PHOTO_URLS
        sizes = [abbrev for abbrev, rname, name in urls]
        if size in sizes:
            return u'%s%s/sizes/%s/' % (
                self.owner.photos_url,
                self.flickr_id,
                size)
        else:
            return u'%s%s/' % (self.owner.photos_url, self.flickr_id)


class Tag(models.Model):
    """
    A Flickr Tag.
    """
    author = models.ForeignKey(
        'flickrsets.Person',
        verbose_name=_('author'),
        related_name='tags')

    flickr_id = models.CharField(
        verbose_name=_('flickr ID'),
        max_length=255)

    name = models.CharField(
        verbose_name=_('name'),
        max_length=255)

    raw = models.CharField(
        verbose_name=_('raw'),
        max_length=255)

    objects = TagManager()

    class Meta:
        """
        Model metadata.
        """
        db_table = '%s_photo_tag' % constants.APP_TABLE_PREFIX
        ordering = ('name',)
        verbose_name = _('tag')
        verbose_name_plural = _('tags')

    def __unicode__(self):
        """
        Object's human readable unicode string.
        """
        return u'%s' % self.name

    @models.permalink
    def get_absolute_url(self):
        """
        Returns object's absolute URL.
        """
        return ('flickrsets-tag', (), {'name': self.name})
