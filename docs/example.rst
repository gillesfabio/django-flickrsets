==============
Example (demo)
==============

You can try `Django Flickrsets`_ with the included example project
(``flickrsets_example`` directory).

Download
========

Grab the project from GitHub::

    git clone git@github.com:gillesfabio/django-flickrsets.git

Installation
============

Pip, virtualenv and virtualenwrapper
------------------------------------

To avoid conflicts and keep your Python environment safe, you should install 
and use `Pip`_ with `virtualenv`_ and `virtualenvwrapper`_::

    easy_install -U pip
    pip install virtualenv
    pip install virtualenvwrapper

Create a directory which will store your virtual environments::

    mkdir $HOME/virtualenvs

In your ``$HOME/.bashrc_profile``, ``$HOME/.bashrc`` or ``$HOME/.profile`` 
file, exports the ``WORKON_HOME`` and ``PIP_VIRTUALENV_BASE`` variables. 

So, add these lines in the file::

    export WORKON_HOME=$HOME/virtualenvs
    export PIP_VIRTUALENV_BASE=$WORKON_HOME

Then, don't forget to load modifications with the ``source`` command::

    source $HOME/your-dot-file

Or, re-open a user session.

Set up the environment
----------------------

Go in ``django-flickrsets/flickrsets_example`` directory::

    cd django-flickrsets/flickrsets_example

Install all requirements in one step using this command::

    pip install -E flickrsets -r requirements.txt

Enable the virtual environment::

    workon flickrsets

Required settings
-----------------

Go in ``django-flickrsets/flickrsets_example`` directory::

    cd django-flickrsets/flickrsets_example

Add a file named ``settings_private.py``::

    touch settings_private.py

This Python module will contain all your private settings. 

In this Python module, define two required settings::

    FLICKRSETS_FLICKR_API_KEY = 'YOUR-FLICKR-API-KEY'
    FLICKRSETS_FLICKR_USER_ID = 'YOUR-FLICKR-USER-ID'

Database stuff
--------------

Synchronizes the database and run migrations::

    python manage.py syncdb
    python manage.py migrate

You can optionally load some testing fixtures::

    python manage.py loaddata flickrsets/tests

See it in the brower
--------------------

Run the server::

    python manage.py runserver

Open your browser and go to http://localhost:8000.

Play with your own sets
-----------------------

Follow the "Administration" chapter.


.. _Django Flickrsets: http://github.com/gillesfabio/django-flickrsets
.. _Pip: http://pip.openplans.org/
.. _virtualenv: http://pypi.python.org/pypi/virtualenv/
.. _virtualenvwrapper: http://pypi.python.org/pypi/virtualenvwrapper
