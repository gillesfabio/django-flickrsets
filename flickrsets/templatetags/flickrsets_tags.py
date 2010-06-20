"""
Templatetags of Django Flickrsets application.
"""
from django import template

from flickrsets import constants

register = template.Library()


class PhotoFlickrUrlsNode(template.Node):
    """
    Process class of ``do_photo_flickr_urls`` template tag.
    """

    def __init__(self, obj, varname='photo_flickr_urls'):
        """
        Initializes the template node.
        """
        self.obj = template.Variable(obj)
        self.varname = varname

    def render(self, context):
        """
        Renders the template node.
        """
        obj = self.obj.resolve(context)
        items = []
        for abbrev, rname, name in constants.FLICKR_PHOTO_URLS:
            item = {}
            item['title'] = name
            item['url'] = obj.get_image_url(size=abbrev)
            items.append(item)
        context[self.varname] = items
        return ''

# pylint: disable=W0613
def do_photo_flickr_urls(parser, token):
    """
    Sets the given ``photo`` object Flickr URLs in the context, stored in the
    template variable ``varname`` or in ``photo_flickr_urls`` variable.
    """
    bits = token.split_contents()
    if len(bits) < 1:
        raise template.TemplateSyntaxError(
            "%r tag requires at least one argument." % bits[0])
    if len(bits) == 3 and bits[2] != "as":
        raise template.TemplateSyntaxError(
            "%r tag third argument must be 'as'." % bits[0])
    if len(bits) > 4:
        raise template.TemplateSyntaxError(
            "%r tag requires takes four arguments maximum." % bits[0])
    kwargs = {}
    if len(bits) >= 2:
        kwargs['obj'] = bits[1]
    if len(bits) == 4:
        kwargs['varname'] = bits[3]
    return PhotoFlickrUrlsNode(**kwargs)


register.tag('flickrsets_get_photo_flickr_urls', do_photo_flickr_urls)
