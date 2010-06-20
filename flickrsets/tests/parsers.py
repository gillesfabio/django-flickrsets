"""
Tests parsers of Django Flickrsets application.
"""
import unittest

from flickrsets import constants
from flickrsets.parsers import PersonParser
from flickrsets.parsers import PhotoParser
from flickrsets.parsers import PhotoTagsParser
from flickrsets.parsers import PhotoExifTagsParser
from flickrsets.parsers import PhotosetParser
from flickrsets.tests.client import FakeClient


class PersonParserTest(unittest.TestCase):
    """
    Tests ``PersonParser`` parser.
    """
    FLICKR_ID = constants.TEST_PERSON_FLICKR_ID
    api_client = FakeClient('apikey')

    def test_raw_data(self):
        """
        Tests ``raw_data`` returned value.
        """
        parser = PersonParser(
            flickr_id=self.FLICKR_ID, 
            client=self.api_client)
        data = parser.raw_data()
        self.assertEquals(data.get('nsid'), self.FLICKR_ID)

    def test_formatted_data(self):
        """
        Tests ``formatted_data`` returned value.
        """
        parser = PersonParser(
            flickr_id=self.FLICKR_ID, 
            client=self.api_client)
        data = parser.formatted_data()
        self.assertEquals(len(data), 1)
        self.assertEquals(data['kwargs']['flickr_id'], self.FLICKR_ID)
        self.assertEquals('fk_fields' in data, False)


class PhotoParserTest(unittest.TestCase):
    """
    Tests ``PhotoParser`` parser.
    """
    FLICKR_ID = constants.TEST_PHOTO_FLICKR_ID
    api_client = FakeClient('apikey')

    def test_raw_data(self):
        """
        Tests ``raw_data`` returned value.
        """
        parser = PhotoParser(
            flickr_id=self.FLICKR_ID, 
            client=self.api_client)
        data = parser.raw_data()
        self.assertEquals(data['id'], self.FLICKR_ID)

    def test_formatted_data(self):
        """
        Tests ``formatted_data`` value.
        """
        parser = PhotoParser(
            flickr_id=self.FLICKR_ID, 
            client=self.api_client)
        data = parser.formatted_data()
        self.assertEquals(len(data), 2)
        self.assertEquals(data['kwargs']['flickr_id'], self.FLICKR_ID)
        self.assertEquals('fk_fields' in data, True)
        self.assertEquals(len(data['fk_fields']), 1)
        self.assertEquals('owner' in data['fk_fields'], True)


class PhotoTagsParserTest(unittest.TestCase):
    """
    Tests ``PhotoTagsParser`` parser.
    """
    FLICKR_ID = constants.TEST_PHOTO_FLICKR_ID
    api_client = FakeClient('apikey')

    def test_raw_data(self):
        """
        Tests ``raw_data`` returned value.
        """
        parser = PhotoTagsParser(
            flickr_id=self.FLICKR_ID, 
            client=self.api_client)
        data = parser.raw_data()
        self.assertEquals(len(data), 3)

    def formatted_data(self):
        """
        Tests ``formatted_data`` returned value.
        """
        parser = PhotoExifTagsParser(
            flickr_id=self.FLICKR_ID, 
            client=self.api_client)   
        data = parser.formatted_data()
        self.assertEquals(len(data), 3)
                
        
class PhotoExifTagsParserTest(unittest.TestCase):
    """
    Tests ``PhotoExifTagsParser`` parser.
    """
    FLICKR_ID = constants.TEST_PHOTO_FLICKR_ID
    api_client = FakeClient('apikey')

    def test_raw_data(self):
        """
        Tests ``raw_data`` returned value.
        """
        parser = PhotoExifTagsParser(
            flickr_id=self.FLICKR_ID, 
            client=self.api_client)   
        data = parser.raw_data()
        self.assertEquals(len(data), 2)

    def formatted_data(self):
        """
        Tests ``formatted_data`` returned value.
        """
        parser = PhotoExifTagsParser(
            flickr_id=self.FLICKR_ID, 
            client=self.api_client)   
        data = parser.formatted_data()
        self.assertEquals(len(data), 2)
        
        spaces = list(set([tag['kwargs']['tag_space'] for tag in data]))
        self.assertEquals(spaces, [u'IPTC', u'ExifIFD'])
        
        tag = data[0]
        self.assertEquals('kwargs' in tag, True)
        self.assertEquals('label' in tag['kwargs'], True)
        self.assertEquals(tag['kwargs']['label'], u'ISO Speed')
        self.assertEquals(tag['kwargs']['raw'], u'400')
        self.assertEquals(tag['kwargs']['tag_space'], u'ExifIFD')
        self.assertEquals(len(tag['kwargs']), 4)


class PhotosetParserTest(unittest.TestCase):
    """
    Tests ``PhotosetParser`` parser.
    """
    FLICKR_ID = constants.TEST_PHOTOSET_FLICKR_ID
    api_client = FakeClient('apikey')

    def test_raw_data(self):
        """
        Tests ``raw_data`` returned value.
        """
        parser = PhotosetParser(
            flickr_id=self.FLICKR_ID, 
            client=self.api_client)
        data = parser.raw_data()
        self.assertEquals(data['id'], self.FLICKR_ID)

    def test_formatted_data(self):
        """
        Tests ``formatted_data`` returned value.
        """
        parser = PhotosetParser(
            flickr_id=self.FLICKR_ID, 
            client=self.api_client)
        data = parser.formatted_data()
        self.assertEquals(len(data), 2)
        self.assertEquals(data['kwargs']['flickr_id'], self.FLICKR_ID)
        self.assertEquals('fk_fields' in data, True)
        self.assertEquals(len(data['fk_fields']), 2)
        self.assertEquals('owner' in data['fk_fields'], True)
        self.assertEquals('primary' in data['fk_fields'], True)
