========
Settings
========

Application's settings that you can define in your project's ``settings`` 
module.

Flickr API
==========

    * ``FLICKRSETS_FLICKR_API_KEY``
        - Description: your Flickr API key
        - Value type: string
        - Default value: ``None``
        
    * ``FLICKRSETS_FLICKR_USER_ID``
        - Description: your Flickr user ID
        - Value type: string
        - Default value: ``None``

Tags
====

    * ``CREATE_TAGS``
        - Description: creates (saves) tags of photos
        - Value type: boolean
        - Default value: ``True``

EXIF Tags
=========

    * ``SAVE_EXIF_TAGS``
        - Description:  saves EXIF tags of photos
        - Value type: boolean
        - Default value: ``True``
        
    * ``EXIF_TAG_SPACE_LIST``
        - Description: EXIF tag spaces to store
        - Value type: list
        - Default value: ``('ExifIFD', 'IPTC')``
        
Views
=====

    * ``FLICKRSETS_PERSON_LIST_VIEW_PAGINATE_BY``
        - Description: number of people to display per page
        - Value type: integer
        - Default value: ``10``

    * ``FLICKRSETS_PERSON_PHOTO_LIST_VIEW_PAGINATE_BY``
        - Description: number of photos to display per page for a given person
        - Value type: integer
        - Default value: ``10``
    
    * ``FLICKRSETS_PHOTO_LIST_VIEW_PAGINATE_BY``
        - Description: number of photos to display per page
        - Value type: integer
        - Default value: ``10``
    
    * ``FLICKRSETS_PHOTOSET_LIST_VIEW_PAGINATE_BY``
        - Description: number of photosets to display per page
        - Value type: integer
        - Default value: ``10``

    * ``FLICKRSETS_PHOTOSET_PHOTO_LIST_VIEW_PAGINATE_BY``
        - Description: number of photos to display per page for a given photoset
        - Value type: integer
        - Default value: ``10``
        
    * ``FLICKRSETS_TAG_PHOTO_LIST_VIEW_PAGINAGE_BY``
        - Description: number of photos to display per page for a given tag
        - Value type: integer
        - Default value: ``10``

Synchronization
===============

    * ``SYNCHRONIZATION_PHOTO_TIME_SLEEP``
        - Description: waiting time between each photo during synchronization
        - Value type: integer or float
        - Default value: ``2``
    
    * ``SYNCHRONIZATION_PHOTOSET_TIME_SLEEP``
        - Description: waiting time between each set during synchronization
        - Value type: integer or float
        - Default value: ``2``
