=============
Configuration
=============

Settings
========

In the ``settings.py`` file of your project, add ``flickrsets`` application to 
``INSTALLED_APPS`` tuple::

    INSTALLED_APPS = (
        ...
        'flickrsets',
        ...
    )
    
You can optionally install ``django.contrib.admin`` application to browse
application's objects or to add new sets for synchronization::

    INSTALLED_APPS = (
        ...
        'django.contrib.admin',
        'flickrsets',
        ...
    )

You also have to define at least two required settings:
    
    * ``FLICKRSETS_FLICKR_API_KEY``: your own Flickr API key
    * ``FLICKRSETS_FLICKR_USER_ID``: your Flickr User ID

Views and URLs
==============

If you want to use the provided views, just include the application's URLs at
the mount point of your choice. Example::

    urlpatterns = patterns('',
        ...
        url(r'^photos/', include('flickrsets.urls')),
    )

By default, Django Flickrsets includes these URLs::

    urlpatterns = patterns('',
        (r'^people/', include('flickrsets.urls.people')),
        (r'^sets/', include('flickrsets.urls.photosets')),
        (r'^tags/', include('flickrsets.urls.tags')),
        (r'', include('flickrsets.urls.photos')),
    )

You can, obviously, override them. 

For example, replace this default include::

    urlpatterns = patterns('',
        ...
        url(r'^photos/', include('flickrsets.urls')),
    )
    
With your own (it is an example)::
    
    urlpatterns = patterns('',
        (r'^photos/photographs/', include('flickrsets.urls.people')),
        (r'^photos/albums/', include('flickrsets.urls.photosets')),
        (r'^photos/tags/', include('flickrsets.urls.tags')),
        (r'', include('flickrsets.urls.photos')),
    )

Tests
=====

To be sure everything's going well, you should run the tests::

    python manage.py test flickrsets
    
Database
========

Define your database settings then synchronize the database to create 
application's tables::

    python manage.py syncdb
    python manage.py migrate


.. _Django Flickrsets: http://github.com/gillesfabio/django-flickrsets
