"""
Administration classes of Django Flickrsets application.
"""
from django.contrib import admin
from django.core.urlresolvers import reverse
from django.db.models.related import RelatedObject
from django.utils.translation import ugettext_lazy as _

from flickrsets import constants
from flickrsets import models


class BaseModelAdmin(admin.ModelAdmin):
    """
    Model admin base class.
    """

    def get_readonly_fields(self, request, obj=None):
        """
        Returns read-only fields.
        """
        if obj is None:
            return
        new_fields = []
        field_names = obj._meta.get_all_field_names()
        for field_name in field_names:
            field = obj._meta.get_field_by_name(field_name)[0]
            if isinstance(field, RelatedObject):
                continue
            if field.primary_key:
                continue
            new_fields.append(field_name)
        return new_fields


class PersonAdmin(BaseModelAdmin):
    """
    Administration class of ``Person`` model.
    """
    list_display = (
        'obj_buddy_icon',
        'name',
        'flickr_id',
        'username',
        'realname',
        'gender',
        'location',
        'obj_urls')
        
    list_filter = (
        'gender',
        'location')
        
    search_fields = (
        'flickr_id',
        'username',
        'realname',
        'location')

    def obj_buddy_icon(self, obj):
        """
        Returns object's buddy icon.
        """
        return u'<img src="%s" alt="%s" />' % (obj.buddy_icon_url, obj.name)
    obj_buddy_icon.allow_tags = True
    obj_buddy_icon.short_description = _('icon')

    def obj_urls(self, obj):
        """
        Returns object's Flickr's URLs.
        """
        links = []
        links.append(u'<a href="%s">%s</a>' % (obj.photos_url, _('photos')))
        links.append(u'<a href="%s">%s</a>' % (obj.profile_url, _('profile')))
        links.append(u'<a href="%s">%s</a>' % (obj.mobile_url, _('mobile')))
        ul = '<ul>'
        for link in links:
            ul += '<li>%s</li>' % link
        ul += '</ul>'
        return ul
    obj_urls.allow_tags = True
    obj_urls.short_description = _('URLs')
    

class PhotoAdmin(BaseModelAdmin):
    """
    Administration class of ``Photo`` model.
    """
    fieldsets = (
        (_('General'), {
            'fields': (
                'title',
                'flickr_id',
                'tags',
                'description',
                'photoset',
                'owner',
                'media',
                'license',
            ),
        }),
        (_('Dates'), {
            'fields': (
                'date_uploaded',
                'date_posted',
                'date_updated',
                'date_taken',
            ),
        }),
        (_('Counts'), {
            'fields': (
                'views_count',
                'comments_count',
            ),
        }),
        (_('Server'), {
            'fields': (
                'farm',
                'server',
                'secret',
                'original_secret',
                'original_format',
            ),
        })
    )
    list_display = (
        'obj_photo',
        'title',
        'flickr_id',
        'obj_photoset',
        'obj_owner',
        'date_uploaded',
        'views_count',
        'comments_count',
        'obj_image_sources',
        'obj_image_urls')
        
    list_filter = (
        'owner',
        'photoset',
        'date_uploaded',
        'media')
        
    search_fields = (
        'title',
        'description',
        'server',
        'farm')

    def obj_photo(self, obj):
        """
        Returns object's photo preview.
        """
        return u'<img src="%s" alt="%s" />' % (
            obj.image_square_source,
            obj.title)
    obj_photo.allow_tags = True
    obj_photo.short_description = _('photo')

    def obj_photoset(self, obj):
        """
        Returns admin link of related ``Photoset`` object.
        """
        return u'<a href="%s">%s</a>' % (
            reverse(
                'admin:flickrsets_photoset_change',
                args=[obj.photoset.pk]),
            obj.photoset)
    obj_photoset.allow_tags = True
    obj_photoset.short_description = _('Photoset')

    def obj_owner(self, obj):
        """
        Returns admin link of related ``Person`` object.
        """
        return u'<a href="%s">%s</a>' % (
            reverse('admin:flickrsets_person_change', args=[obj.owner.pk]),
            obj.owner)
    obj_owner.allow_tags = True
    obj_owner.short_description = _('owner')

    def obj_image_sources(self, obj):
        """
        Returns object's image sources.
        """
        sources = u'<ul>'
        for abbrev, rname, name in constants.FLICKR_PHOTO_SOURCES:
            source_url = getattr(obj, 'image_%s_source' % rname)
            sources += u'<li><a href="%s">%s</a></li>' % (source_url, name)
        sources += u'</ul>'
        return sources
    obj_image_sources.allow_tags = True
    obj_image_sources.short_description = _('files')

    def obj_image_urls(self, obj):
        """
        Returns object's image URLs.
        """
        urls = u'<ul>'
        for abbrev, rname, name in constants.FLICKR_PHOTO_URLS:
            size_url = getattr(obj, 'image_%s_url' % rname)
            urls += u'<li><a href="%s">%s</a></li>' % (size_url, name)
        urls += u'</ul>'
        return urls
    obj_image_urls.allow_tags = True
    obj_image_urls.short_description = _('URLs')


class PhotosetAdmin(BaseModelAdmin):
    """
    Administration class of ``Photoset`` model.
    """
    list_display = (
        '__unicode__',
        'obj_owner',
        'photos_count')
        
    list_filter = ('owner',)
    
    search_fields = (
        'title',
        'description',
        'server',
        'farm')

    def obj_owner(self, obj):
        """
        Returns admin link of related ``Person`` object (owner)
        """
        return u'<a href="%s">%s</a>' % (
            reverse('admin:flickrsets_person_change', args=[obj.owner.pk]),
            obj.owner.name)
    obj_owner.allow_tags = True
    obj_owner.short_description = _('owner')


class RegisteredSetAdmin(admin.ModelAdmin):
    """
    Administration class of ``RegisteredSet`` model.
    """
    list_display = (
        'title',
        'flickr_id',
        'enabled')


admin.site.register(models.Person, PersonAdmin)
admin.site.register(models.Photo, PhotoAdmin)
admin.site.register(models.Photoset, PhotosetAdmin)
admin.site.register(models.RegisteredSet, RegisteredSetAdmin)
