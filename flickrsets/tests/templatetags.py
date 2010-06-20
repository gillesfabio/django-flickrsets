"""
Tests template tags of Django Flickrsets application.
"""
from django import template
from django import test

from flickrsets import constants
from flickrsets.models import Photo


class TemplateTagTest(test.TestCase):
    """
    Helper class.
    """

    def install_tag_library(self, library):
        """
        Installs tag library.
        """
        template.libraries[library] = __import__(library)

    def render_template(self, template_string, **context):
        """
        Renders template.
        """
        t = template.Template(template_string)
        c = template.Context(context)
        return t.render(c)


class PhotoFlickrUrlsNodeTest(TemplateTagTest):
    """
    Tests ``PhotoFlickrUrlsNode`` class.
    """
    fixtures = ['flickrsets/tests']

    def setUp(self):
        """
        Sets up the test.
        """
        self.install_tag_library('flickrsets.templatetags.flickrsets_tags')

    def test_render(self):
        """
        Tests the render.
        """
        photo = Photo.objects.get(flickr_id=constants.TEST_PHOTO_FLICKR_ID)
        items = []
        for abbrev, rname, name in constants.FLICKR_PHOTO_URLS:
            item = {}
            item['title'] = name
            item['url'] = photo.get_image_url(size=abbrev)
            items.append(item)
        should_output = u''
        for item in items:
            should_output += u'%s - %s' % (item['title'], item['url'])
        output = self.render_template((
            "{% load flickrsets_tags %}"
            "{% flickrsets_get_photo_flickr_urls photo %}"
            "{% for url in photo_flickr_urls %}"
            "{{ url.title }} - {{ url.url }}"
            "{% endfor %}"),
            photo=photo)
        self.assertEquals(output, should_output)
