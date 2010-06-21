==============
Administration
==============

Adding Flickr sets to synchronize via the admin
===============================================

Go in the admin and add Flickr sets you want to synchronize by adding new
*registered set* objects.

For each set, two required fields:

    * ``flickr_id``: The Flickr set ID
    * ``title``: The Flickr set Title (just to identify the set, not displayed)
    * ``enabled``: enable or disable the set for synchronization

Never ever add/delete/change *Person*, *Photoset*, *Photo* and *Tag* objects.
They are managed by the application.

Adding Flickr sets to synchronize via the CLI
=============================================

`Django Flickrsets`_ adds ``fsets`` command to Django command list.

Take a look by invoking ``manage.py`` without any argument::

    python manage.py
    
This command provides commands to help you managing your Flickr sets:

    * ``flush``: flushes existing tables
    * ``sync``: synchronizes registered Flickr sets with Flickr
    * ``add``: registers a new Flickr set for synchronization
    * ``remove``: removes (deletes) a registered Flickr set
    * ``list``: lists all registered Flickr sets
    * ``enable``: enables a disabled Flickr set
    * ``disable``: disables an enabled Flickr set

The ``fsets add`` command lists all public sets of the Flickr User previously
defined in ``settings.FLICKRSETS_FLICKR_USER_ID``. 

The other ones (``remove``, ``list``, ``enable``, ``disable``), help
you managing *registered set* objects stored in the database.

.. _Django Flickrsets: http://github.com/gillesfabio/django-flickrsets
