"""
Flickr client of Django Flickrsets application.

Client's code is borrowed from Jacob Kaplan-Moss Jellyroll project
(http://github.com/jacobian/jellyroll).
"""
import urllib

from flickrsets import utils


class FlickrError(Exception):
    """
    A Flickr Error Exception.
    """

    def __init__(self, code, message):
        """
        Initializes exception.
        """
        self.code = code
        self.message = message

    def __str__(self):
        """
        Exception human readable string.
        """
        return u'FlickrError %s: %s' % (self.code, self.message)


class FlickrClient(object):
    """
    The Flickr Client.
    """

    def __init__(self, api_key, method='flickr'):
        """
        Initializes the Flickr client.
        """
        self.api_key = api_key
        self.method = method

    def __getattr__(self, method):
        """
        Catches Flickr API methods.
        """
        return FlickrClient(self.api_key, '%s.%s' % (self.method, method))

    def __repr__(self):
        """
        Object's representation.
        """
        return '<FlickrClient: %s>' % self.method

    def __call__(self, **params):
        """
        Maps Flickr API methods.
        """
        params['method'] = self.method
        params['api_key'] = self.api_key
        params['format'] = 'json'
        params['nojsoncallback'] = '1'
        url = 'http://flickr.com/services/rest/?' + urllib.urlencode(params)
        json = utils.get_json(url)
        if json.get('stat', '') == 'fail':
            raise FlickrError(json['code'], json['message'])
        return json
