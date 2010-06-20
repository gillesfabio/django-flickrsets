"""
Tests of Flickr API client of Django Flickrsets application.
"""
from __future__ import with_statement

import mock
import unittest

from flickrsets import utils
from flickrsets.client import FlickrClient
from flickrsets.client import FlickrError


class FlickrClientTest(unittest.TestCase):
    """
    Tests ``FlickrClient`` class.
    """

    def test_client_getattr(self):
        """
        Tests ``__getattr__`` method.
        """
        c1 = FlickrClient('apikey')
        self.assertEquals(c1.api_key, 'apikey')
        self.assertEquals(c1.method, 'flickr')

        c2 = c1.foo.bar.baz
        self.assertEquals(c2.api_key, 'apikey')
        self.assertEquals(c2.method, 'flickr.foo.bar.baz')

    def test_client_call(self):
        """
        Tests ``__call__`` method.
        """
        mock_get_json = mock.Mock(return_value={})
        with mock.patch_object(utils, 'get_json', mock_get_json) as mocked:
            c = FlickrClient('apikey')
            res = c.foo.bar(a=1, b=2)
            self.assert_(mocked.called)

    def test_client_call_fail(self):
        """
        Tests ``__call__`` method which fails.
        """
        failure = {'stat': 'fail', 'code': 1, 'message': 'fail'}
        mock_get_json = mock.Mock(return_value=failure)
        with mock.patch_object(utils, 'get_json', mock_get_json):
            c = FlickrClient('apikey')
            self.assertRaises(FlickrError, c.foo)


# Fake client
# -----------------------------------------------------------------------------
FakeClient = mock.Mock()
FakeClient.return_value = FakeClient

# Person
FakeClient.people.getInfo.return_value = {
    "person": {
        "username": {
            "_content": "gillesfabio"
        },
        "photosurl": {
            "_content": "http://www.flickr.com/photos/gillesfabio/"
        },
        "nsid": "94238521@N00",
        "path_alias": "gillesfabio",
        "photos": {
            "count": {
                "_content": 660
            },
            "firstdatetaken": {
                "_content": "2005-12-10 20:34:19"
            },
            "firstdate": {
                "_content": "1183230521"
            }
        },
        "iconserver": "118",
        "profileurl": {
            "_content": "http://www.flickr.com/people/gillesfabio/"
        },
        "mobileurl": {
            "_content": "http://m.flickr.com/photostream.gne?id=3179235"
        },
        "ispro": 1,
        "location": {
            "_content": "Saint-Laurent-du-Var, France"
        },
        "id": "94238521@N00",
        "realname": {
            "_content": "Gilles Fabio"
        },
        "iconfarm": 1
    },
    "stat": "ok"
}

# Photo
FakeClient.photos.getInfo.return_value = {
    "photo": {
        "dateuploaded": "1262561502",
        "originalformat": "jpg",
        "owner": {
            "username": "gillesfabio",
            "realname": "Gilles Fabio",
            "nsid": "94238521@N00",
            "location": "Saint-Laurent-du-Var, France"
        },
        "id": "4242733600",
        "title": {
            "_content": "Mozart Opera Rock"
        },
        "media": "photo",
        "tags": {
            "tag": [
                {
                    "raw": "bokeh",
                    "machine_tag": 0,
                    "id": "3179235-4242733600-4796",
                    "_content": "bokeh",
                    "author": "94238521@N00"
                },
                {
                    "raw": "mozart",
                    "machine_tag": 0,
                    "id": "3179235-4242733600-44656",
                    "_content": "mozart",
                    "author": "94238521@N00"
                },
                {
                    "raw": "music",
                    "machine_tag": 0,
                    "id": "3179235-4242733600-326",
                    "_content": "music",
                    "author": "94238521@N00"
                },
            ]
        },
        "comments": {
            "_content": "2"
        },
        "secret": "4a3364d8a9",
        "usage": {
            "canblog": 0,
            "canshare": 0,
            "candownload": 1,
            "canprint": 0
        },
        "description": {
            "_content": ""
        },
        "isfavorite": 0,
        "views": "22",
        "farm": 5,
        "rotation": 0,
        "dates": {
            "taken": "2010-01-03 17:15:33",
            "lastupdate": "1275542160",
            "takengranularity": "0",
            "posted": "1262561502"
        },
        "originalsecret": "288ebc9494",
        "license": "0",
        "notes": {
            "note": []
        },
        "server": "4032",
    },
    "stat": "ok"
}

# Exif tags
FakeClient.photos.getExif.return_value = {
    "photo": {
        "farm": 5,
        "secret": "4a3364d8a9",
        "id": "4242733600",
        "exif": [
            {
                "raw": {
                    "_content": "400"
                },
                "tagspace": "ExifIFD",
                "tagspaceid": 0,
                "tag": "ISO",
                "label": "ISO Speed"
            },
            {
                "raw": {
                    "_content": "Gilles Fabio"
                },
                "tagspace": "IPTC",
                "tagspaceid": 0,
                "tag": "CopyrightNotice",
                "label": "Copyright Notice"
            },
        ],
        "server": "4032"
    },
    "stat": "ok"
}

# Tags
FakeClient.tags.getListPhoto.return_value = {
    "photo": {
        "id": "4242733600", 
        "tags": {
            "tag": [
                {
                    "machine_tag": 0, 
                    "_content": "bokeh", 
                    "author": "94238521@N00", 
                    "raw": "bokeh", 
                    "authorname": "gillesfabio", 
                    "id": "3179235-4242733600-4796"
                }, 
                {
                    "machine_tag": 0, 
                    "_content": "mozart", 
                    "author": "94238521@N00", 
                    "raw": "mozart", 
                    "authorname": "gillesfabio", 
                    "id": "3179235-4242733600-44656"
                }, 
                {
                    "machine_tag": 0, 
                    "_content": "music", 
                    "author": "94238521@N00", 
                    "raw": "music", 
                    "authorname": "gillesfabio", 
                    "id": "3179235-4242733600-326"
                }, 
            ]
        }
    }, 
    "stat": "ok"
}

# Photoset
FakeClient.photosets.getInfo.return_value = {
    "stat": "ok",
    "photoset": {
        "description": {
            "_content": ""
        },
        "title": {
            "_content": "Misc"
        },
        "farm": 5,
        "primary": "4242733600",
        "server": "4032",
        "photos": 3,
        "secret": "4a3364d8a9",
        "owner": "94238521@N00",
        "id": "72157623007721343"
    }
}

FakeClient.photosets.getPhotos.return_value = {
    "stat": "ok",
    "photoset": {
        "perpage": 500,
        "photo": [
            {
                "title": "Mozart Opera Rock",
                "farm": 5,
                "server": "4032",
                "secret": "4a3364d8a9",
                "isprimary": "1",
                "id": "4242733600"
            },
            {
                "title": "Self-portrait",
                "farm": 3,
                "server": "2786",
                "secret": "8dc4026bc2",
                "isprimary": "0",
                "id": "4242740086"
            },
            {
                "title": "Candle",
                "farm": 5,
                "server": "4010",
                "secret": "f7dd8201be",
                "isprimary": "0",
                "id": "4242741774"
            }
        ],
        "pages": 1,
        "primary": "4242733600",
        "id": "72157623007721343",
        "ownername": "gillesfabio",
        "owner": "94238521@N00",
        "per_page": 500,
        "total": "3",
        "page": 1
    }
}
