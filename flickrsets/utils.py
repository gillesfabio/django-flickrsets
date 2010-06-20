"""
Utils of Django Flickrsets application.
"""
import datetime
import re

import dateutil.parser
import dateutil.tz
import httplib2
from django.utils import simplejson
from django.utils.encoding import force_unicode

DEFAULT_HTTP_HEADERS = {
    "User-Agent": "Django Flickrsets/0.1",
}

DATETIME_STRING_RE = ("(?P<year>[0-9]{4})-(?P<month>[0-9]{2})-"
                      "(?P<day>[0-9]{2}) (?P<hour>[0-9]{2}):(?P<min>[0-9]{2}):"
                      "(?P<sec>[0-9]{2})")
                      

def fetch_resource(url, method='GET', body=None, username=None, password=None,
    headers=None):
    """
    Fetches and parsers a resource.
    """
    h = httplib2.Http(timeout=15)
    h.force_exception_to_status_code = True
    if username is not None or password is not None:
        h.add_credentials(username, password)
    if headers is None:
        headers = DEFAULT_HTTP_HEADERS.copy()
    response, content = h.request(url, method, body, headers)
    return content


def get_json(url, **kwargs):
    """
    Fetches and parses some JSON. Returns the deserialized JSON.
    """
    json = fetch_resource(url, **kwargs)
    return simplejson.loads(json)


def parse_date(string):
    """
    Converts a string into a (local, naive) datetime object.
    """
    if re.match(DATETIME_STRING_RE, string):
        dt = dateutil.parser.parse(string)
        if dt.tzinfo:
            dt = dt.astimezone(dateutil.tz.tzlocal()).replace(tzinfo=None)
    else:
        dt = datetime.datetime.fromtimestamp(safe_int(string))
    return dt


def safe_int(string):
    """
    Always returns an integer. Returns 0 on failure.
    """
    try:
        return int(force_unicode(string))
    except (ValueError, TypeError):
        return 0
