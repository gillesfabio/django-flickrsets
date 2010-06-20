===============
Example project
===============

You can try `Django Flickrsets`_ with the included example project
(``flickrsets_example`` directory). 

Set up the project::

    git clone git@github.com:gillesfabio/django-flickrsets.git
    cd django-flickrsets/flickrsets_example
    pip install -E flickrsets -r requirements.txt
    workon flickrsets
    touch settings_private.py

In ``settings_private.py`` file, add the two required settings::

    FLICKRSETS_FLICKR_API_KEY = 'YOUR-FLICKR-API-KEY'
    FLICKRSETS_FLICKR_USER_ID = 'YOUR-FLICKR-USER-ID'

Then::

    python manage.py syncdb
    python manage.py loaddata flickrsets/tests
    python manage.py runserver
    
Open your browser and go to http://localhost:8000.

.. _Django Flickrsets: http://github.com/gillesfabio/django-flickrsets
