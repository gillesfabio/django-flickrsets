"""
Manager classes of Django Flickrsets application.
"""
import logging

from django.db import models

log = logging.getLogger('flickrsets.managers')


class PersonManager(models.Manager):
    """
    Manager of ``Person`` model.
    """
    
    def get_or_create_from_api(self, flickr_id, client):
        """
        Returns a ``Person`` object or creates it from Flickr API.

        Takes two required arguments:
        
            * ``flickr_id``: Photo's Flickr ID
            * ``client``: ``FlickrClient`` instance
            
        Returns a tuple of ``(object, created)``, where ``created`` is a
        boolean specifying wether an object was created.
        """
        try:
            return self.get(flickr_id=flickr_id), False
        except self.model.DoesNotExist:
            obj = self.create_object_from_api(
                flickr_id=flickr_id, 
                client=client)
            return obj, True

    def create_object_from_api(self, flickr_id, client):
        """
        Creates a new ``Person`` object from Flickr API.
        
        Takes two required arguments:
        
            * ``flickr_id``: Photo's Flickr ID
            * ``client``: ``FlickrClient`` instance

        """
        from flickrsets import parsers
        parser = parsers.PersonParser(flickr_id=flickr_id, client=client)
        data = parser.formatted_data()
        obj = self.create(**data['kwargs'])
        log.info(u'Created new person: "%s"' % obj.name)
        return obj


class PhotoManager(models.Manager):
    """
    Manager of ``Photo`` model.
    """

    def get_or_create_from_api(self, flickr_id, client, **kwargs):
        """
        Returns a ``Photo`` object or creates it from Flickr API.
        
        Takes two required arguments:
        
            * ``flickr_id``: Photo's Flickr ID
            * ``client``: ``FlickrClient`` instance
            
        Returns a tuple of ``(object, created)``, where ``created`` is a
        boolean specifying wether an object was created.
        """
        try:
            return self.get(flickr_id=flickr_id), False
        except self.model.DoesNotExist:
            obj = self.create_object_from_api(
                flickr_id=flickr_id, 
                client=client, 
                **kwargs)
            return obj, True

    def create_object_from_api(self, flickr_id, client, photoset=None,
        create_tags=False, create_exif_tags=False):
        """
        Creates a new ``Photo`` object from Flickr API.
        
        Takes two required arguments:
        
            * ``flickr_id``: Photo's Flickr ID
            * ``client``: ``FlickrClient`` instance
            
        Takes three optional arguments:
        
            * ``photoset``: a ``Photoset`` object to add as foreign key
            * ``create_tags``: create related ``Tag`` objects?
            * ``create_exif_tags``: create related ``ExifTag`` objects?
            
        """
        from flickrsets import parsers
        from flickrsets.models import ExifTag
        from flickrsets.models import Person
        from flickrsets.models import Tag
        
        parser = parsers.PhotoParser(flickr_id=flickr_id, client=client)
        data = parser.formatted_data()

        owner, created = Person.objects.get_or_create_from_api(
            flickr_id=data['fk_fields']['owner'],
            client=client)
        data['kwargs']['owner'] = owner
        log.info(u'"%s" added as owner of photo "%s"' % (
            owner.name, 
            data['kwargs']['title']))
        
        if photoset is not None:
            data['kwargs']['photoset'] = photoset
            log.debug(u'"%s" added as photoset of photo "%s"' % (
                photoset.title,
                data['kwargs']['title']))

        photo = self.create(**data['kwargs'])
        log.info(u'Created new photo: "%s"' % photo.title)

        if create_tags:
            objects, created = Tag.objects.filter_or_create_from_api(
                photo=photo,
                client=client)
                
        if create_exif_tags:
            objects, created = ExifTag.objects.filter_or_create_from_api(
                photo=photo, 
                client=client)
        
        return photo


class PhotosetManager(models.Manager):
    """
    Manager of ``Photoset`` model.
    """
    def get_or_create_from_api(self, flickr_id, client, **kwargs):
        """
        Returns a ``Photoset`` object or creates it from Flickr API.
        
        Takes two required arguments:
        
            * ``flickr_id``: Photoset's Flickr ID
            * ``client``: ``FlickrClient`` instance
            
        Returns a tuple of ``(object, created)``, where ``created`` is a
        boolean specifying wether an object was created.
        """
        try:
            return self.get(flickr_id=flickr_id), False
        except self.model.DoesNotExist:
            obj = self.create_object_from_api(
                flickr_id=flickr_id,
                client=client,
                **kwargs)
            return obj, True

    def create_object_from_api(self, flickr_id, client, related_kwargs=None):
        """
        Creates a new ``Photoset`` object from Flickr API.
        
        Takes two required arguments:
        
            * ``flickr_id``: Photoset's Flickr ID
            * ``client``: ``FlickrClient`` instance

        Takes one optional argument:

            * ``related_kwargs``: keyword arguments passed to related objects

        """
        from flickrsets import parsers
        from flickrsets.models import Person
        from flickrsets.models import Photo
        from flickrsets.models import Photoset

        parser = parsers.PhotosetParser(flickr_id=flickr_id, client=client)
        data = parser.formatted_data()
        
        if related_kwargs is None:
            related_kwargs = {}
        
        if 'primary' not in related_kwargs:
            related_kwargs['primary'] = {}
            
        owner, created = Person.objects.get_or_create_from_api(
            flickr_id=data['fk_fields']['owner'],
            client=client)
            
        data['kwargs']['owner'] = owner
        log.info(u'"%s" added as owner of photoset "%s"' % (
            owner.name, 
            data['kwargs']['title']))

        primary, created = Photo.objects.get_or_create_from_api(
            flickr_id=data['fk_fields']['primary'],
            client=client,
            **related_kwargs['primary'])
            
        data['kwargs']['primary'] = primary
        log.info(u'"%s" added as primary of photoset "%s"' % (
            primary.title,
            data['kwargs']['title']))

        obj = Photoset.objects.create(**data['kwargs'])
        log.info(u'Created new photoset: "%s"' % obj.title)

        primary.photoset = obj
        primary.save()
        log.info(u'"%s" added as photoset of primary photo "%s"' % (
            obj.title,
            primary.title))

        return obj

    def get_photos_ids_from_api(self, flickr_id, client):
        """
        Returns Flickr IDs of photoset's photos from Flickr API.
        
        Takes two required arguments:
        
            * ``flickr_id``: Photoset's Flickr ID
            * ``client``: ``FlickrClient`` instance
            
        """
        from flickrsets import parsers
        parser = parsers.PhotosetParser(flickr_id=flickr_id, client=client)
        return parser.get_photos_ids()


class TagManager(models.Manager):
    """
    Manager of ``Tag`` model.
    """

    def filter_or_create_from_api(self, photo, client):
        """
        Returns related ``Tag`` objects of the given ``photo`` object or 
        creates them from Flickr API.
        
        Takes two required arguments:
        
            * ``photo``: ``Photo`` object
            * ``client``: ``FlickrClient`` instance
            
        Returns a tuple of ``(objects, created)``, where ``created`` is a
        boolean specifying wether objects was created.
        """
        objects = photo.tags.all()
        if objects:
            return objects, False
        else:
            objects = self.create_objects_from_api(photo=photo, client=client)
            return objects, True

    def create_objects_from_api(self, photo, client):
        """
        Creates related ``Tag`` objects of the given ``photo`` object from
        Flickr API.
        
        Takes two required arguments:
        
            * ``photo``: ``Photo`` object
            * ``client``: ``FlickrClient`` instance

        """
        from flickrsets import parsers
        from flickrsets.models import Person
        
        parser = parsers.PhotoTagsParser(
            flickr_id=photo.flickr_id, 
            client=client)
        
        objects = []
        
        for tag in parser.formatted_data():
            try:
                obj = self.get(raw=tag['kwargs']['raw'])
                objects.append(obj)
            except self.model.DoesNotExist:                
                author, created = Person.objects.get_or_create_from_api(
                    flickr_id=tag['fk_fields']['author'],
                    client=client)
                tag['kwargs']['author'] = author
                obj = self.create(**tag['kwargs'])
                objects.append(obj)
                log.info(u'Created new tag: "%s"' % obj.name)
            photo.tags.add(obj)
            log.info(u'Tagged "%s" with tag "%s"' % (photo, obj))
        
        return objects


class ExifTagManager(models.Manager):
    """
    Manager of ``ExifTag`` model.
    """

    def filter_or_create_from_api(self, photo, client):
        """
        Returns related ``ExifTag`` objects of the given ``photo`` object or 
        creates them from Flickr API.
        
        Takes two required arguments:
        
            * ``photo``: ``Photo`` object
            * ``client``: ``FlickrClient`` instance
            
        Returns a tuple of ``(objects, created)``, where ``created`` is a
        boolean specifying wether objects was created.
        """
        objects = self.filter(photo=photo)     
        if objects:
            return objects, False
        else:
            objects = self.create_objects_from_api(photo=photo, client=client)
            return objects, True

    def create_objects_from_api(self, photo, client):
        """
        Creates related ``Tag`` objects of the given ``photo`` object from
        Flickr API.
        
        Takes two required arguments:
        
            * ``photo``: ``Photo`` object
            * ``client``: ``FlickrClient`` instance
            
        """
        from flickrsets import parsers
        
        parser = parsers.PhotoExifTagsParser(
            flickr_id=photo.flickr_id, 
            client=client)
        
        objects = []
        
        for exif_tag in parser.formatted_data():
            obj = self.create(photo=photo, **exif_tag['kwargs'])
            objects.append(obj)
            log.info(u'Created new EXIF tag: "%s"' % obj)
        
        return objects


class RegisteredSetManager(models.Manager):
    """
    Manager of ``RegisteredSet`` model.
    """

    def enabled(self):
        """
        Only returns enabled sets.
        """
        return self.filter(enabled=True)

    def disabled(self):
        """
        Only returns disabled sets.
        """
        return self.filter(enabled=False)
