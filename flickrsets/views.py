"""
Views of Django Flickrsets application.
"""
from django import shortcuts
from django.views.generic import list_detail

from flickrsets import settings as app_settings
from flickrsets.models import Person
from flickrsets.models import Photo
from flickrsets.models import Photoset
from flickrsets.models import Tag


def person_list(request, queryset=None, **kwargs):
    """
    Displays ``Person`` object list.
    
    This is a short wrapper around the generic ``list_detail.object_list`` 
    view. So, all context variables populated by that view will be available 
    here. 
    
    Additionally, any keyword arguments which are valid for this generic
    view will be accepted and passed to it.
    
    Default values are:
    
        * ``queryset``: ``Person.objects.all()``
        * ``template_name``: ``flickrsets/person/list.html``
        * ``template_object_name``: ``person``
        * ``paginate_by``: ``settings.FLICKRSETS_PERSON_LIST_VIEW_PAGINATE_BY``
        
    """
    if queryset is None:
        queryset = Person.objects.all()
    
    if 'queryset' in kwargs:
        del kwargs['queryset']
        
    if 'template_name' not in kwargs:
        kwargs['template_name'] = 'flickrsets/person/list.html'
    
    if 'template_object_name' not in kwargs:
        kwargs['template_object_name'] = 'person'
    
    if 'paginate_by' not in kwargs:
        kwargs['paginate_by'] = getattr(
            app_settings,
            'PERSON_LIST_VIEW_PAGINATE_BY')
            
    return list_detail.object_list(request, queryset, **kwargs)


def person_photo_list(request, flickr_id, queryset=None, **kwargs):
    """
    Displays ``Photo`` object list of a given ``Person`` object.
    
    Takes one required argument:
    
        * ``flickr_id``: the Flickr ID of the given person
        
    This is a short wrapper around the generic ``list_detail.object_list`` 
    view. So, all context variables populated by that view will be available 
    here. One extra variable is added:
    
        * ``person``: the given ``Person`` object
    
    Additionally, any keyword arguments which are valid for this generic
    view will be accepted and passed to it.
    
    Default values are:
    
        * ``queryset``: ``person.photos.all()`` (``person`` is the given ``Person`` object)
        * ``template_name``: ``flickrsets/person/photo_list.html``
        * ``template_object_name``: ``photo``
        * ``paginate_by``: ``settings.FLICKRSETS_PERSON_PHOTO_LIST_VIEW_PAGINATE_BY``

    """
    if queryset is None:
        queryset = Person.objects.all()
        
    if 'queryset' in kwargs:
        del kwargs['queryset']
        
    if 'template_name' not in kwargs:
        kwargs['template_name'] = 'flickrsets/person/photo_list.html'
    
    if 'template_object_name' not in kwargs:
        kwargs['template_object_name'] = 'photo'
    
    if 'paginate_by' not in kwargs:
        kwargs['paginate_by'] = getattr(
            app_settings,
            'PERSON_PHOTO_LIST_VIEW_PAGINATE_BY')
            
    person = shortcuts.get_object_or_404(queryset, flickr_id=flickr_id)

    if 'extra_context' not in kwargs:
        kwargs['extra_context'] = {}
    kwargs['extra_context']['person'] = person
    
    queryset = person.photos.all()
    
    return list_detail.object_list(request, queryset, **kwargs)


def photo_list(request, queryset=None, **kwargs):
    """
    Displays ``Photo`` object list.
    
    This is a short wrapper around the generic ``list_detail.object_list`` 
    view. So, all context variables populated by that view will be available 
    here. 
    
    Additionally, any keyword arguments which are valid for this generic
    view will be accepted and passed to it.
    
    Default values are:
    
        * ``queryset``: ``Photo.objects.all()``
        * ``template_name``: ``flickrsets/photo/list.html``
        * ``template_object_name``: ``photo``
        * ``paginate_by``: ``settings.FLICKRSETS_PHOTO_LIST_VIEW_PAGINATE_BY``
        
    """
    if queryset is None:
        queryset = Photo.objects.all()
    
    if 'queryset' in kwargs:
        del kwargs['queryset']
        
    if 'template_name' not in kwargs:
        kwargs['template_name'] = 'flickrsets/photo/list.html'
    
    if 'template_object_name' not in kwargs:
        kwargs['template_object_name'] = 'photo'
    
    if 'paginate_by' not in kwargs:
        kwargs['paginate_by'] = getattr(
            app_settings,
            'PHOTO_LIST_VIEW_PAGINATE_BY')
            
    return list_detail.object_list(request, queryset, **kwargs)


def photo_detail(request, flickr_id, queryset=None, **kwargs):
    """
    Displays a given ``Photo`` object.
    
    Takes one required argument:
    
        * ``flickr_id``: the given photo Flickr ID
        
    This is a short wrapper around the generic ``list_detail.object_detail`` 
    view. So, all context variables populated by that view will be available 
    here. 
    
    Additionally, any keyword arguments which are valid for this generic
    view will be accepted and passed to it.
    
    Default values are:
    
        * ``queryset``: ``Photo.objects.all()``
        * ``slug``: ``flickr_id``
        * ``slug_field``: ``flickr_id``
        * ``template_name``: ``flickrsets/photo/detail.html``
        * ``template_object_name``: ``photo``
        
    """
    if queryset is None:
        queryset = Photo.objects.all()
    
    for key in ('queryset', 'slug'):
        if key in kwargs:
            del kwargs[key]
    
    kwargs['slug'] = flickr_id
    
    if 'slug_field' not in kwargs:
        kwargs['slug_field'] = 'flickr_id'
    
    if 'template_name' not in kwargs:
        kwargs['template_name'] = 'flickrsets/photo/detail.html'
    
    if 'template_object_name' not in kwargs:
        kwargs['template_object_name'] = 'photo'
    
    return list_detail.object_detail(request, queryset, **kwargs)


def photoset_list(request, queryset=None, **kwargs):
    """
    Displays ``Photoset`` object list.
    
    This is a short wrapper around the generic ``list_detail.object_list`` 
    view. So, all context variables populated by that view will be available 
    here. 
    
    Additionally, any keyword arguments which are valid for this generic
    view will be accepted and passed to it.
    
    Default values are:
    
        * ``queryset``: ``Photoset.objects.all()``
        * ``template_name``: ``flickrsets/photoset/list.html``
        * ``template_object_name``: ``photoset``
        * ``paginate_by``: ``settings.FLICKRSETS_PHOTOSET_LIST_VIEW_PAGINATE_BY``
        
    """
    if queryset is None:
        queryset = Photoset.objects.all()
    
    if 'queryset' in kwargs:
        del kwargs['queryset']
        
    if 'template_name' not in kwargs:
        kwargs['template_name'] = 'flickrsets/photoset/list.html'
    
    if 'template_object_name' not in kwargs:
        kwargs['template_object_name'] = 'photoset'
    
    if 'paginate_by' not in kwargs:
        kwargs['paginate_by'] = getattr(
            app_settings,
            'PHOTOSET_LIST_VIEW_PAGINATE_BY')
            
    return list_detail.object_list(request, queryset, **kwargs)


def photoset_photo_list(request, flickr_id, queryset=None, **kwargs):
    """
    Displays ``Photo`` object list of a given ``Photoset`` object.
    
    Takes one required argument:
    
        * ``flickr_id``: the given photoset Flickr ID
        
    This is a short wrapper around the generic ``list_detail.object_list`` 
    view. So, all context variables populated by that view will be available 
    here. One extra variable is added:
    
        * ``photoset``: the given ``Photoset`` object
    
    Additionally, any keyword arguments which are valid for this generic
    view will be accepted and passed to it.
    
    Default values are:
    
        * ``queryset``: ``photoset.photos.all()`` (``photoset`` is the given ``Photoset`` object)
        * ``template_name``: ``flickrsets/photoset/photo_list.html``
        * ``template_object_name``: ``photo``
        * ``paginate_by``: ``settings.FLICKRSETS_PHOTOSET_PHOTO_LIST_VIEW_PAGINATE_BY``

    """
    if queryset is None:
        queryset = Photoset.objects.all()
        
    if 'queryset' in kwargs:
        del kwargs['queryset']
        
    if 'template_name' not in kwargs:
        kwargs['template_name'] = 'flickrsets/photoset/photo_list.html'
    
    if 'template_object_name' not in kwargs:
        kwargs['template_object_name'] = 'photo'
    
    if 'paginate_by' not in kwargs:
        kwargs['paginate_by'] = getattr(
            app_settings,
            'PHOTOSET_PHOTO_LIST_VIEW_PAGINATE_BY')
            
    photoset = shortcuts.get_object_or_404(queryset, flickr_id=flickr_id)

    if 'extra_context' not in kwargs:
        kwargs['extra_context'] = {}
    kwargs['extra_context']['photoset'] = photoset
    
    queryset = photoset.photos.all()
    
    return list_detail.object_list(request, queryset, **kwargs)


def tag_list(request, queryset=None, **kwargs):
    """
    Displays ``Tag`` object list.
    
    This is a short wrapper around the generic ``list_detail.object_list`` 
    view. So, all context variables populated by that view will be available 
    here. 
    
    Additionally, any keyword arguments which are valid for this generic
    view will be accepted and passed to it.
    
    Default values are:
    
        * ``queryset``: ``Tag.objects.all()``
        * ``template_name``: ``flickrsets/tag/list.html``
        * ``template_object_name``: ``tag``

    """
    if queryset is None:
        queryset = Tag.objects.all()
    
    if 'queryset' in kwargs:
        del kwargs['queryset']
        
    if 'template_name' not in kwargs:
        kwargs['template_name'] = 'flickrsets/tag/list.html'
    
    if 'template_object_name' not in kwargs:
        kwargs['template_object_name'] = 'tag'
            
    return list_detail.object_list(request, queryset, **kwargs)


def tag_photo_list(request, name, queryset=None, **kwargs):
    """
    Displays ``Photo`` object list of a given ``Tag`` object.
    
    Takes one required argument:
    
        * ``name``: the given tag name
        
    This is a short wrapper around the generic ``list_detail.object_list`` 
    view. So, all context variables populated by that view will be available 
    here. One extra variable is added:
    
        * ``tag``: the given ``Tag`` object
    
    Additionally, any keyword arguments which are valid for this generic
    view will be accepted and passed to it.
    
    Default values are:
    
        * ``queryset``: ``tag.photos.all()`` (``tag`` is the given ``Tag`` object)
        * ``template_name``: ``flickrsets/tag/photo_list.html``
        * ``template_object_name``: ``photo``
        * ``paginate_by``: ``settings.FLICKRSETS_TAG_PHOTO_LIST_VIEW_PAGINATE_BY``

    """
    if queryset is None:
        queryset = Tag.objects.all()
        
    if 'queryset' in kwargs:
        del kwargs['queryset']
        
    if 'template_name' not in kwargs:
        kwargs['template_name'] = 'flickrsets/tag/photo_list.html'
    
    if 'template_object_name' not in kwargs:
        kwargs['template_object_name'] = 'photo'
    
    if 'paginate_by' not in kwargs:
        kwargs['paginate_by'] = getattr(
            app_settings,
            'TAG_PHOTO_LIST_VIEW_PAGINATE_BY')
            
    tag = shortcuts.get_object_or_404(queryset, name=name)

    if 'extra_context' not in kwargs:
        kwargs['extra_context'] = {}
    kwargs['extra_context']['tag'] = tag
    
    queryset = tag.photos.all()
    
    return list_detail.object_list(request, queryset, **kwargs)
