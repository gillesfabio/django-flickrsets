"""
Models tests of Django Flickrsets application.
"""
import unittest

from django import test
from django.core.urlresolvers import reverse

from flickrsets import constants
from flickrsets.models import ExifTag
from flickrsets.models import Person
from flickrsets.models import Photo
from flickrsets.models import Photoset
from flickrsets.models import Tag
from flickrsets.tests.client import FakeClient


class PersonTest(test.TestCase):
    """
    Tests ``Person`` model.
    """
    fixtures = ['flickrsets/tests']

    def setUp(self):
        """
        Sets up the test.
        """
        self.person = Person.objects.get(
            flickr_id=constants.TEST_PERSON_FLICKR_ID)

    def test_unicode(self):
        """
        Tests ``__unicode__`` value.
        """
        self.assertEquals(self.person.__unicode__(), self.person.name)

    def test_get_absolute_url(self):
        """
        Tests ``get_absolute_url`` method.
        """
        url = reverse('flickrsets-person', args=[self.person.flickr_id])
        self.assertEquals(self.person.get_absolute_url(), url)

    def test_name(self):
        """
        Tests ``name`` property.
        """
        self.assertEquals(self.person.name, u'Gilles Fabio')
        
        person = Person.objects.create(
            flickr_id=u'FOOBAR',
            photos_url=self.person.photos_url,
            profile_url=self.person.profile_url,
            mobile_url=self.person.mobile_url)   
        self.assertEquals(person.name, u'FOOBAR')
        person.username = u'superfoobar'
        person.save()
        self.assertEquals(person.name, u'superfoobar')
        
        person.realname = u'Super Foo Bar'
        person.save()
        self.assertEquals(person.name, u'Super Foo Bar')
        
        person.delete()

    def test_default_gender(self):
        """
        Tests default ``gender`` field value.
        """
        self.assertEquals(self.person.gender, constants.FLICKR_DEFAULT_GENDER)
        
        person = Person.objects.create(
            flickr_id=u'FOOBAR',
            photos_url=self.person.photos_url,
            profile_url=self.person.profile_url,
            mobile_url=self.person.mobile_url)
        self.assertEquals(person.gender, constants.FLICKR_DEFAULT_GENDER)
        
        person.gender = constants.FLICKR_GENDER_OTHER
        person.save()
        self.assertEquals(person.gender, constants.FLICKR_GENDER_OTHER)
        
        person.delete()

    def test_buddy_icon_url(self):
        """
        Tests ``buddy_icon_url`` property.
        """
        url = u'http://farm%s.static.flickr.com/%s/buddyicons/%s.jpg' % (
            self.person.icon_farm,
            self.person.icon_server,
            self.person.flickr_id)
        self.assertEquals(self.person.buddy_icon_url, url)
        
        person = Person.objects.create(
            flickr_id=u'FOOBAR',
            photos_url=self.person.photos_url,
            profile_url=self.person.profile_url,
            mobile_url=self.person.mobile_url)
        default_url = u'http://www.flickr.com/images/buddyicon.jpg'            
        self.assertEquals(person.buddy_icon_url, default_url)
        
        person.delete()


class PersonManagerTest(unittest.TestCase):
    """
    Tests ``PersonManager`` manager.
    """
    FLICKR_ID = constants.TEST_PERSON_FLICKR_ID
    api_client = FakeClient('apikey')

    def test_create_object_from_api(self):
        """
        Tests ``create_object_from_api`` method.
        """
        person = Person.objects.create_object_from_api(
            flickr_id=self.FLICKR_ID, 
            client=self.api_client)
        self.assertEquals(person.flickr_id, self.FLICKR_ID)
        self.assertEquals(person.name, u'Gilles Fabio')
        
        Person.objects.all().delete()
        self.assertEquals(Person.objects.all().count(), 0)

    def test_get_or_create_from_api(self):
        """
        Tests ``get_or_create_from_api`` method.
        """
        person, created = Person.objects.get_or_create_from_api(
            flickr_id=self.FLICKR_ID, 
            client=self.api_client)
        self.assertEquals(created, True)
        self.assertEquals(person.flickr_id, self.FLICKR_ID)
        self.assertEquals(person.name, u'Gilles Fabio')

        person, created = Person.objects.get_or_create_from_api(
            flickr_id=self.FLICKR_ID, 
            client=self.api_client)
        self.assertEquals(created, False)
        self.assertEquals(person.flickr_id, self.FLICKR_ID)
        self.assertEquals(person.name, u'Gilles Fabio')

        Person.objects.all().delete()
        self.assertEquals(Person.objects.all().count(), 0)


class PhotoTest(test.TestCase):
    """
    Tests ``Photo`` model.
    """
    fixtures = ['flickrsets/tests']

    def setUp(self):
        """
        Sets up the test.
        """
        self.photo = Photo.objects.get(
            flickr_id=constants.TEST_PHOTO_FLICKR_ID)

    def test_unicode(self):
        """
        Tests ``__unicode__`` method.
        """
        self.assertEquals(self.photo.__unicode__(), self.photo.title)

    def test_get_absolute_url(self):
        """
        Tests ``get_absolute_url`` method
        """
        url = reverse('flickrsets-photo', args=[self.photo.flickr_id])
        self.assertEquals(self.photo.get_absolute_url(), url)

    def test_image_source(self):
        """
        Tests ``image_source`` property and ``image_VERSION_source`` dynamic
        properties.
        """
        for abbrev, rname, name in constants.FLICKR_PHOTO_SOURCES:
            if abbrev != constants.FLICKR_PHOTO_SOURCE_MEDIUM:
                secret = self.photo.secret
                if abbrev == constants.FLICKR_PHOTO_SOURCE_ORIGINAL:
                    secret = self.photo.original_secret
                url = u'http://farm%s.static.flickr.com/%s/%s_%s_%s.jpg' % (
                    self.photo.farm,
                    self.photo.server,
                    self.photo.flickr_id,
                    secret,
                    abbrev)
                photo_url = getattr(self.photo, 'image_%s_source' % rname)
                self.assertEquals(photo_url, url)
                
        default_url = u'http://farm%s.static.flickr.com/%s/%s_%s.jpg' % (
            self.photo.farm,
            self.photo.server,
            self.photo.flickr_id,
            self.photo.secret)
        self.assertEquals(self.photo.image_source, default_url)

    def test_image_url(self):
        """
        Tests ``image_url`` property and ``image_VERSION_url`` dynamic
        properties.
        """
        for abbrev, rname, name in constants.FLICKR_PHOTO_URLS:
            url = u'%s%s/sizes/%s/' % (
                self.photo.owner.photos_url,
                self.photo.flickr_id,
                abbrev)
            photo_url = getattr(self.photo, 'image_%s_url' % rname)
            self.assertEquals(photo_url, url)
            
        default_url = u'%s%s/' % (
            self.photo.owner.photos_url,
            self.photo.flickr_id)
        self.assertEquals(self.photo.get_image_url(size='foo'), default_url)


class PhotoManagerTest(unittest.TestCase):
    """
    Tests ``PhotoManager`` manager.
    """
    FLICKR_ID = constants.TEST_PHOTO_FLICKR_ID
    api_client = FakeClient('apikey')

    def test_create_object_from_api(self):
        """
        Tests ``create_object_from_api`` method.
        """
        photo = Photo.objects.create_object_from_api(
            flickr_id=self.FLICKR_ID, 
            client=self.api_client,
            create_tags=False,
            create_exif_tags=False)
        self.assertEquals(photo.flickr_id, self.FLICKR_ID)
        self.assertEquals(photo.title, u'Mozart Opera Rock')

        Photo.objects.all().delete()
        self.assertEquals(Photo.objects.all().count(), 0)

    def test_get_or_create_from_api(self):
        """
        Tests ``get_or_create_from_api`` method.
        """
        photo, created = Photo.objects.get_or_create_from_api(
            flickr_id=self.FLICKR_ID, 
            client=self.api_client,
            create_tags=False,
            create_exif_tags=False)
        self.assertEquals(created, True)
        self.assertEquals(photo.flickr_id, self.FLICKR_ID)
        self.assertEquals(photo.title, u'Mozart Opera Rock')

        photo, created = Photo.objects.get_or_create_from_api(
            flickr_id=self.FLICKR_ID, 
            client=self.api_client,
            create_tags=False,
            create_exif_tags=False)
        self.assertEquals(created, False)
        self.assertEquals(photo.flickr_id, self.FLICKR_ID)
        self.assertEquals(photo.title, u'Mozart Opera Rock')

        Photo.objects.all().delete()
        self.assertEquals(Photo.objects.all().count(), 0)


class PhotosetTest(test.TestCase):
    """
    Tests ``Photoset`` model.
    """
    fixtures = ['flickrsets/tests']

    def setUp(self):
        """
        Sets up the test.
        """
        self.photoset = Photoset.objects.get(
            flickr_id=constants.TEST_PHOTOSET_FLICKR_ID)

    def test_unicode(self):
        """
        Tests ``__unicode__`` method.
        """
        self.assertEquals(self.photoset.__unicode__(), self.photoset.title)

    def test_get_absolute_url(self):
        """
        Tests ``get_absolute_url`` method.
        """
        url = reverse('flickrsets-photoset', args=[self.photoset.flickr_id])
        self.assertEquals(self.photoset.get_absolute_url(), url)

    def test_get_flickr_url(self):
        """
        Tests ``get_flickr_url`` method.
        """
        url = u'http://flickr.com/photos/%s/sets/%s/' % (
            self.photoset.owner.photos_url,
            self.photoset.flickr_id)
        self.assertEquals(self.photoset.get_flickr_url(), url)


class PhotosetManagerTest(unittest.TestCase):
    """
    Tests ``PhotosetManager`` manager.
    """
    FLICKR_ID = constants.TEST_PHOTOSET_FLICKR_ID
    api_client = FakeClient('apikey')

    def test_create_object_from_api(self):
        """
        Tests ``create_object_from_api`` method.
        """
        photoset = Photoset.objects.create_object_from_api(
            flickr_id=self.FLICKR_ID, 
            client=self.api_client)
        self.assertEquals(photoset.flickr_id, self.FLICKR_ID)
        self.assertEquals(photoset.title, u'Misc')

        Photoset.objects.all().delete()
        self.assertEquals(Photoset.objects.all().count(), 0)

    def test_get_or_create_from_api(self):
        """
        Tests ``get_or_create_from_api`` method.
        """
        photoset, created = Photoset.objects.get_or_create_from_api(
            flickr_id=self.FLICKR_ID, 
            client=self.api_client)
        self.assertEquals(created, True)
        self.assertEquals(photoset.flickr_id, self.FLICKR_ID)
        self.assertEquals(photoset.title, u'Misc')

        photoset, created = Photoset.objects.get_or_create_from_api(
            flickr_id=self.FLICKR_ID, 
            client=self.api_client)
        self.assertEquals(created, False)
        self.assertEquals(photoset.flickr_id, self.FLICKR_ID)
        self.assertEquals(photoset.title, u'Misc')

        Photoset.objects.all().delete()
        self.assertEquals(Photoset.objects.all().count(), 0)


class TagTest(test.TestCase):
    """
    Tests ``Photo`` model.
    """
    fixtures = ['flickrsets/tests']

    def setUp(self):
        """
        Sets up the test.
        """
        self.tag = Tag.objects.get(raw=constants.TEST_TAG_RAW)

    def test_unicode(self):
        """
        Tests ``__unicode__``  method.
        """
        self.assertEquals(self.tag.__unicode__(), self.tag.name)

    def test_get_absolute_url(self):
        """
        Tests ``get_absolute_url`` method.
        """
        url = reverse('flickrsets-tag', args=[self.tag.raw])
        self.assertEquals(self.tag.get_absolute_url(), url)


class TagManagerTest(unittest.TestCase):
    """
    Tests ``TagManager`` manager.
    """
    PHOTO_FLICKR_ID = constants.TEST_PHOTO_FLICKR_ID
    api_client = FakeClient('apikey')

    def test_create_objects_from_api(self):
        """
        Tests ``create_objects_from_api`` method.
        """
        photo, created = Photo.objects.get_or_create_from_api(
            flickr_id=self.PHOTO_FLICKR_ID,
            client=self.api_client,
            create_tags=False,
            create_exif_tags=False)
        self.assertEquals(created, True)
        self.assertEquals(photo.title, u'Mozart Opera Rock')
    
        Tag.objects.all().delete()
        self.assertEquals(Tag.objects.all().count(), 0)
           
        tags = Tag.objects.create_objects_from_api(
            photo=photo,
            client=self.api_client)   
        self.assertEquals(len(tags), 3)
        
        Tag.objects.all().delete()
        self.assertEquals(Tag.objects.all().count(), 0)
        
        Photo.objects.all().delete()
        self.assertEquals(Photo.objects.all().count(), 0)

    def test_filter_or_create_from_api(self):
        """
        Tests ``filter_or_create_from_api`` method.
        """
        photo, created = Photo.objects.get_or_create_from_api(
            flickr_id=self.PHOTO_FLICKR_ID,
            client=self.api_client,
            create_tags=False,
            create_exif_tags=False)
        self.assertEquals(created, True)
        self.assertEquals(photo.title, u'Mozart Opera Rock')
        
        Tag.objects.all().delete()
        self.assertEquals(Tag.objects.all().count(), 0)
        
        tags, created = Tag.objects.filter_or_create_from_api(
            photo=photo, 
            client=self.api_client)
        self.assertEquals(created, True)
        self.assertEquals(len(tags), 3)
        
        tags, created = Tag.objects.filter_or_create_from_api(
            photo=photo,
            client=self.api_client)   
        self.assertEquals(created, False)
        self.assertEquals(len(tags), 3)
        
        Tag.objects.all().delete()
        self.assertEquals(Tag.objects.all().count(), 0)

        Photo.objects.all().delete()
        self.assertEquals(Photo.objects.all().count(), 0)


class ExifTagTest(test.TestCase):
    """
    Tests ``ExifTag`` model.
    """
    fixtures = ['flickrsets/tests']

    def setUp(self):
        """
        Sets up the test.
        """
        self.tag = ExifTag.objects.get(
            photo__flickr_id=constants.TEST_PHOTO_FLICKR_ID,
            label='ISO Speed')

    def __unicode__(self):
        """
        Tests ``__unicode__`` method.
        """
        name = u'%s -- %s: %s' % (
            self.tag.photo,
            self.tag.label,
            self.tag.clean or self.tag.raw)

        self.assertEquals(self.tag.__unicode__(), name)


class ExifTagManagerTest(unittest.TestCase):
    """
    Tests ``ExifTagManager`` manager.
    """
    PHOTO_FLICKR_ID = constants.TEST_PHOTO_FLICKR_ID
    api_client = FakeClient('apikey')

    def test_create_objects_from_api(self):
        """
        Tests ``create_objects_from_api`` method.
        """
        photo, photo_created = Photo.objects.get_or_create_from_api(
            flickr_id=self.PHOTO_FLICKR_ID,
            client=self.api_client)   
        exif_tags = ExifTag.objects.create_objects_from_api(
            photo=photo,
            client=self.api_client)   
        self.assertEquals(len(exif_tags), 2)
        
        ExifTag.objects.all().delete()
        self.assertEquals(ExifTag.objects.all().count(), 0)

        Photo.objects.all().delete()
        self.assertEquals(Photo.objects.all().count(), 0)

    def test_filter_or_create_from_api(self):
        """
        Tests ``filter_or_create_from_api`` method.
        """
        photo, created = Photo.objects.get_or_create_from_api(
            flickr_id=self.PHOTO_FLICKR_ID,
            client=self.api_client)
        exif_tags, created = ExifTag.objects.filter_or_create_from_api(
            photo=photo,
            client=self.api_client)   
        self.assertEquals(created, True)
        self.assertEquals(len(exif_tags), 2)

        exif_tags, created = ExifTag.objects.filter_or_create_from_api(
            photo=photo,
            client=self.api_client)   
        self.assertEquals(created, False)
        self.assertEquals(len(exif_tags), 2)
        
        ExifTag.objects.all().delete()
        self.assertEquals(ExifTag.objects.all().count(), 0)

        Photo.objects.all().delete()
        self.assertEquals(Photo.objects.all().count(), 0)
