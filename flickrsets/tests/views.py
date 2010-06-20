"""
Views tests of Django Flickrsets application.
"""
from django import test
from django.core.urlresolvers import reverse

from flickrsets.models import Person
from flickrsets.models import Photo
from flickrsets.models import Photoset
from flickrsets.models import Tag


class ViewsTest(test.TestCase):
    """
    Views tests.
    """
    fixtures = ['flickrsets/tests']

    def test_person_list(self):
        """
        Tests ``person_list`` view.
        """
        response = self.client.get(reverse('flickrsets-people'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'flickrsets/person/list.html')

    def test_person_photo_list(self):
        """
        Tests ``person_photo_list`` view.
        """
        people = Person.objects.all()
        for person in people:
            response = self.client.get(
                reverse('flickrsets-person', args=[person.flickr_id]))
            self.assertEquals(response.status_code, 200)
            self.assertTemplateUsed(response, 'flickrsets/person/photo_list.html')

    def test_person_photo_list_404(self):
        """
        Tests 404 on ``person_photo_list`` view
        """
        response = self.client.get(
            reverse('flickrsets-person', args=['unknown']))
        self.assertEquals(response.status_code, 404)

    def test_photo_list(self):
        """
        Tests ``photo_list`` view.
        """
        response = self.client.get(reverse('flickrsets-photos'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'flickrsets/photo/list.html')

    def test_photo_detail(self):
        """
        Tests ``photo_detail`` view.
        """
        photos = Photo.objects.all()
        for photo in photos:
            response = self.client.get(
                reverse('flickrsets-photo', args=[photo.flickr_id]))
            self.assertEquals(response.status_code, 200)
            self.assertTemplateUsed(response, 'flickrsets/photo/detail.html')

    def test_photo_detail_404(self):
        """
        Tests 404 on ``photo_detail`` view.
        """
        response = self.client.get(
            reverse('flickrsets-photo', args=['unknown']))
        self.assertEquals(response.status_code, 404)

    def test_photoset_list(self):
        """
        Tests ``photoset_list`` view.
        """
        response = self.client.get(reverse('flickrsets-photosets'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'flickrsets/photoset/list.html')

    def test_photoset_photo_list(self):
        """
        Tests ``photoset_photo_list`` view.
        """
        photosets = Photoset.objects.all()
        for photoset in photosets:
            response = self.client.get(
                reverse('flickrsets-photoset', args=[photoset.flickr_id]))
            self.assertEquals(response.status_code, 200)
            self.assertTemplateUsed(response, 'flickrsets/photoset/photo_list.html')

    def test_photoset_photo_list_404(self):
        """
        Tests 404 on ``photoset_photo_list`` view
        """
        response = self.client.get(
            reverse('flickrsets-photoset', args=['unknown']))
        self.assertEquals(response.status_code, 404)

    def test_tag_list(self):
        """
        Tests ``tag_list`` view.
        """
        response = self.client.get(reverse('flickrsets-tags'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'flickrsets/tag/list.html')

    def test_tag_photo_list(self):
        """
        Tests ``tag_photo_list`` view.
        """
        tags = Tag.objects.all()
        for tag in tags:
            response = self.client.get(
                reverse('flickrsets-tag', args=[tag.name]))
            self.assertEquals(response.status_code, 200)
            self.assertTemplateUsed(response, 'flickrsets/tag/photo_list.html')

    def test_tag_photo_list_404(self):
        """
        Tests 404 on ``tag_photo_list`` view.
        """
        response = self.client.get(
            reverse('flickrsets-tag', args=['unknown']))
        self.assertEquals(response.status_code, 404)
